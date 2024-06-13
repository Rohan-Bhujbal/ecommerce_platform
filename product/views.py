from django.http import JsonResponse
from product.product import ProductController
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from user.models import User

# Add Product
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def product_add_view(request):
    try:
        request_data = request.POST.copy()
        user_id = request.user.id if request.user.is_authenticated else None
        user = request.user if request.user.is_authenticated else None
        if user_id is None or user is None:
            super_admin = User.objects.get(user_type='admin')
            user_id = super_admin.id
            user = super_admin
        product_controller = ProductController()
        is_active = request.POST.get('is_active',True)
        if is_active == 'true':
            is_active = True
        else:
            is_active = False
        
        if 'request' not in request_data:
            request_data['request'] = {
                'product_name': request.POST.get('product_name'),
                'short_description': request.POST.get('short_description'),
                'mrp': request.POST.get('mrp'),
                'is_active': is_active,
                # 'product_image': request.FILES['product_image',]
            }
        response_data = product_controller.product_add(request_data, user_id, user)
        return JsonResponse(response_data['response'], status=200 if response_data['response']['status'] == 200 else 400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# Edit product
@csrf_exempt
@api_view(["PUT"])
@permission_classes((AllowAny,))
def product_edit_view(request):
    try:
        request_data = request.POST.copy()
        user_id = request.user.id if request.user.is_authenticated else None
        user = request.user if request.user.is_authenticated else None
        if user_id is None or user is None:
            super_admin = User.objects.get(user_type='admin')
            user_id = super_admin.id
            user = super_admin
        product_controller = ProductController()
        is_active = request.POST.get('is_active',True)
        if is_active == 'true':
            is_active = True
        else:
            is_active = False
        is_return = request.POST.get('is_return',True)
        if is_return == 'true':
            is_return = True
        else:
            is_return = False
        if 'request' not in request_data:
            request_data['request'] = {
                'product_id':request.POST.get('product_id'),
                'product_name': request.POST.get('product_name'),
                'short_description': request.POST.get('short_description'),
                'mrp': request.POST.get('mrp'),
                'is_active': is_active,
                # 'product_image': request.FILES['product_image']
            }
        response_data = product_controller.product_edit(request_data, user_id, user)
        return JsonResponse(response_data['response'], status=200 if response_data['response']['status'] == 200 else 400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# Product List 
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def product_list_view(request):
    try:
        request_data = request.POST.copy()
        user_id = request.user.id if request.user.is_authenticated else None
        user = request.user if request.user.is_authenticated else None
        if user_id is None or user is None:
            super_admin = User.objects.get(user_type='admin')
            user_id = super_admin.id
            user = super_admin
        product_controller = ProductController()
        status = request.GET.get('status', 'true')
        if status == 'true':
            status =True
        else:
            status = False
        if 'request' not in request_data:
            request_data['request'] = {
                'page_no': request.GET.get('page_no','1'),
                'limit': request.GET.get('limit','20'),
                'status': status,
                'search': request.GET.get('search'),
                'order_by': request.GET.get('order_by')
            }
        response_data = product_controller.product_list(request_data, user_id, user)
        return JsonResponse(response_data['response'], status=200 if response_data['response']['status'] == 200 else 400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)