from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from user.models import User
from order.order import OrderController



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def order_add_view(request):
    try:
        request_data = request.POST.copy()
        user_id = request.user.id if request.user.is_authenticated else None
        user = request.user if request.user.is_authenticated else None
        if user_id is None or user is None:
            super_admin = User.objects.get(user_type='admin')
            user_id = super_admin.id
            user = super_admin
        order_controller = OrderController()
        if 'request' not in request_data:
            request_data['request'] = {
                'total_qty' : request.POST.get('total_qty'),
                'product_id' : request.POST.get('product_id')    
            }
        response_data = order_controller.order_add(request_data, user_id, user)
        return JsonResponse(response_data['response'], status=200 if response_data['response']['status'] == 200 else 400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def order_list_view(request):
    try:
        request_data = {
            "request": {
                "limit": request.GET.get("limit", "20"),
                "page_no": request.GET.get("page_no", "1"),
            }
        }
        user_id = request.user.id if request.user.is_authenticated else None
        user = request.user if request.user.is_authenticated else None
        if user_id is None or user is None:
            super_admin = User.objects.get(user_type='admin')
            user_id = super_admin.id
            user = super_admin
        order_controller = OrderController()
        response_data = order_controller.order_list(request_data, user_id, user)
        return JsonResponse(response_data['response'], status=200 if response_data['response']['status'] == 200 else 400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)