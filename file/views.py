import uuid
from file import messages
from file.models import UserFile
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from file.helpers import file_helper_func
from app.globals import (
    VAR_FILE, 
    VAR_THUMBNAIL, 
    FILE_TYPE,
)
from file.files import (
    save_file,
    view_local_file,
    get_s3_file_url,  
    get_s3_thumb_url,
    get_file_details,
)
from django.views.decorators.clickjacking import xframe_options_exempt
from user.auth import is_login
from app.messages import SOMETHING_WENT_WRONG


@csrf_exempt
@api_view(["POST"])
def upload_file(request):
    user = request.user
    data = request.data
    user_id = str(user.id)

    if 'file' in request.FILES:
        file_obj = request.FILES['file']
        if file_obj:
            data = file_helper_func(file_obj, user_id)
            if data:
                return JsonResponse(data, safe=False)
            else:
                return JsonResponse({VAR_FILE: SOMETHING_WENT_WRONG}, status=400)
        else:
            return JsonResponse({VAR_FILE: messages.INVALID_AUTH}, status=400)
    return JsonResponse({VAR_FILE: messages.INVALID_FILE}, status=400)


@csrf_exempt
@api_view(["GET"])
def get_file_detail(request, file_id):
    user_file_dict = {}
    user_file_dict = get_file_details(file_id)
    if user_file_dict:
        return JsonResponse(user_file_dict, safe=False)
    else:
        return JsonResponse({VAR_FILE: messages.FILE_NOT_FOUND}, status=400)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
@xframe_options_exempt
def download_file(request, type, id):
    if is_login(request):
        if type in FILE_TYPE:
            if type == VAR_THUMBNAIL:
                try:
                    user_file = UserFile.objects.get(id=uuid.UUID(id).hex)
                except UserFile.DoesNotExist:
                    return JsonResponse({VAR_FILE: messages.FILE_NOT_FOUND}, status=400)
                if user_file:
                    if user_file.is_350_thumb:
                        path = get_s3_thumb_url(str(user_file.user_id), str(user_file.name))
                    else:
                        res = view_local_file(VAR_THUMBNAIL, user_file.name)
                        if res:
                            return res
                        else:
                            return JsonResponse({ "error": messages.FILE_VIEW_FIELD}, status=400)
            else:
                try:
                    user_file = UserFile.objects.get(id=uuid.UUID(id).hex)
                except UserFile.DoesNotExist:
                    return JsonResponse({VAR_FILE: messages.FILE_NOT_FOUND+"."}, status=400)
                if user_file:
                    if user_file.is_s3_url:
                        path = get_s3_file_url(str(user_file.user_id), str(user_file.name))
                    else:
                        res = view_local_file(VAR_FILE, user_file.name)
                        if res:
                            return res
                        else:
                            return JsonResponse({ "error": messages.FILE_VIEW_FIELD}, status=400)

            return save_file(path.split("com")[-1])
        else:
            return JsonResponse({ "error": messages.ENTER_CORRECT_FILE_TYPE}, status=400)
    else:
        return JsonResponse({ "error": messages.INVALID_AUTH}, status=400)
