import uuid
import json

from user.user import UserController
from . import messages
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from user.models import User, UserMagicCode
from django.views.decorators.csrf import csrf_exempt
from user.auth import get_user_dict, user_logout, auth_token, check_user_pass
from rest_framework.decorators import api_view, permission_classes
from app.helper import(
    email_validate,
)

from user.helper import (
    get_login_user,
    remove_html_tags,
    get_response,
    session_timeout,
)
from user.validations import (
    login_validation,
    magic_code_validation,
)
from app.globals import BAD_CODE, OK_CODE
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_exempt
from app.messages import SOMETHING_WENT_WRONG


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    Method : Login

    Args:
        request : Self para

    Returns:
        Successful user object with access token
    """
    response = {}
    try:
        res = json.loads(request.body)
        vr = login_validation.validate(res)
        if vr.get('success', False) is False:
            res['error'] = vr.get("error")
            return JsonResponse(res, status=BAD_CODE)
        email = email_validate(res.get('email').lower())
        password = res.get('password')
        device_type = res.get("device_type").lower()
        device_id = res.get("device_id")
        if email:
            try:
                user = User.objects.exclude(deleted_at__isnull=False).get(email=email)
            except User.DoesNotExist:
                response['error'] = messages.USER_EMAIL_NOT_REGISTERED
                return JsonResponse(response, status=BAD_CODE)

            if check_user_pass(password, user.password):
                response['msg'] = messages.USER_LOGIN_SUCCESS
                response['data'] = get_login_user(user, request, device_type, device_id)
                return JsonResponse(response, safe=False)
            else:
                response['error'] = messages.WRONG_PASS
                return JsonResponse(response, status=BAD_CODE)
        else:
            response['error'] = messages.PLEASE_PROVIDE_VALID_EMAIL
            return JsonResponse(response, status=BAD_CODE)
    except Exception as e:
        response['error'] = repr(e)
        return JsonResponse(response, status=BAD_CODE)


@csrf_exempt
@api_view(["GET"])
def get_user(request):
    res = {}
    res['msg'] = messages.USER_LANDING_SUCCESS
    res['data'] = get_user_dict(request.user)
    return JsonResponse(res, safe=False)


@csrf_exempt
@api_view(["GET"])
def logout(request):
    response = {}
    user_token =  user_logout(auth_token(request))
    if user_token:
        response['msg'] = messages.USER_LOGOUT_SUCCESS
        response['data'] = user_token
        return JsonResponse(response, safe=False)
    else:
        response['error'] = SOMETHING_WENT_WRONG
        return JsonResponse(response, status=BAD_CODE)
    


@csrf_exempt
@api_view(["POST"])
def get_magic_code(request):
    response_data = get_response()
    res = json.loads(request.body)
    vr = magic_code_validation.validate(res)
    if vr.get('success', False) is False:
        response_data['errors'] = vr.get("error")
        return JsonResponse(response_data, status=400)
    device_type = remove_html_tags(res.get('device_type'))
    device_id = remove_html_tags(res.get('device_id'))
    magic_code = uuid.uuid4()
    user_magic_code = UserMagicCode(id=magic_code, user_id=request.user.id, device_id=device_id, device_type=device_type, magic_code=str(magic_code))
    user_magic_code.save()
    if user_magic_code:
        response_data['data'] = magic_code
        return JsonResponse(response_data, safe=False)
    else:
        response_data['errors'] = messages.TOKEN_NOT_FOUND
        return JsonResponse(response_data, safe=False, status=400)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def set_login(request, magic_code, device_id, device_type):
    user_magic_code = UserMagicCode.objects.filter(
                magic_code=magic_code, device_id=device_id, device_type=device_type).first()
    if user_magic_code:
        if session_timeout(user_magic_code) :
            request.session['user_id'] = str(user_magic_code.user_id)
            user_magic_code.delete()
            return HttpResponseRedirect(str(settings.REDIRECT_LOGIN))
    response_data = get_response()
    response_data['errors'] = messages.TOKEN_NOT_FOUND
    return JsonResponse(response_data, safe=False, status=400)


@csrf_exempt
@api_view(["GET"])
@xframe_options_exempt
@permission_classes((AllowAny,))
def get_login(request):
    response_data = get_response()
    if 'user_id' in request.session:
        response_data['data'] = request.session['user_id']
        return JsonResponse(response_data, safe=False)
    else:
        response_data['errors'] = messages.TOKEN_NOT_FOUND
        return JsonResponse(response_data, safe=False, status=400)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def del_login(request):
    try:
        del request.session['user_id']
    except:
        pass
    return HttpResponseRedirect(str(settings.REDIRECT_LOGOUT))


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def user_add_view(request):
    try:
        request_data = request.POST.copy()
        user_id = request.user.id if request.user.is_authenticated else None
        user = request.user if request.user.is_authenticated else None
        if user_id is None or user is None:
            super_admin = User.objects.get(user_type='super_admin')
            user_id = super_admin.id
            user = super_admin
        user_controller = UserController()
        is_active = request.POST.get('is_active',True)
        if is_active == 'true':
            is_active = True
        else:
            is_active = False
        if 'request' not in request_data:
            request_data['request'] = {
                'full_name' : request.get('full_name'),
                'email' : request.get('email'),
                'mobile' : request.get('mobile'),
                'address' : request.get('address'),
                'password' : request.get('password'),
                'user_type' : request.get('user_type'),
                'permissions' : request.get('permissions'),
                'related_id' : request.get('related_id'),
                'is_active': is_active
            }
        response_data = user_controller.user_add(request_data, user_id, user)
        return JsonResponse(response_data['response'], status=200 if response_data['response']['status'] == 200 else 400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
@api_view(["PUT"])
@permission_classes((AllowAny,))
def user_edit_view(request):
    try:
        request_data = request.POST.copy()
        user_id = request.user.id if request.user.is_authenticated else None
        user = request.user if request.user.is_authenticated else None
        if user_id is None or user is None:
            super_admin = User.objects.get(user_type='super_admin')
            user_id = super_admin.id
            user = super_admin
        user_controller = UserController()
        is_active = request.POST.get('is_active',True)
        if is_active == 'true':
            is_active = True
        else:
            is_active = False
        if 'request' not in request_data:
            request_data['request'] = {
                'user_id' : request.POST.get('user_id'),
                'full_name' : request.POST.get('full_name'),
                'email' : request.POST.get('email'),
                'mobile' : request.POST.get('mobile'),
                'address' : request.POST.get('address'),
                'password' : request.POST.get('password'),
                'user_type' : request.POST.get('user_type'),
                'permissions' : request.POST.get('permissions'),
                'related_id' : request.POST.get('related_id'),
                'is_active': is_active
            }
        response_data = user_controller.user_add(request_data, user_id, user)
        return JsonResponse(response_data['response'], status=200 if response_data['response']['status'] == 200 else 400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def user_list_view(request):
    try:
        request_data = {}
        user = request.user if request.user.is_authenticated else None
        if not user:
            super_admin = User.objects.get(user_type='admin')
            user = super_admin
        user_id = user.id
        status = request.GET.get("status", "true")
        if status == 'true':
            status =True
        else:
            status = False
        page_no = request.GET.get("page_no","1")
        limit = request.GET.get("limit","10")
        search = request.GET.get("search")
        user_type = request.GET.get('user_type')
        order_by = request.GET.get("order_by", "-updated_at")
        if 'request' not in request_data:
            request_data['request'] = {
                "page_no": page_no,
                "limit": limit,
                "status": status,
                "search": search,
                "user_type": user_type,
                "order_by": order_by
            }
        user_controller = UserController()
        response_data = user_controller.user_list(request_data, user_id, user)
        return JsonResponse(response_data['response'], status=200 if response_data['response']['status'] == 200 else 400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)