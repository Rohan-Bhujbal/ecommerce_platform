from product.validations import (
    product_validation,
)
import uuid
from app.helper import ws_response
from product.helper import product_already_exists, get_product_code
from product.dict import product_dict
from product import messages
from product.models import Product
from app.globals import BAD_CODE, OK_CODE
from app.helper import pagination_validation, get_paginated_response
from django.db.models import Q


class ProductController:

    def product_add(self, request_data, user_id, user):
        request = False
        if "request" in request_data:
            request = request_data.get("request")
        try:
            if 'product_image' in request:
                product_image = request.get('product_image')
                del request['product_image']
            else:
                product_image =None
            if 'is_active' in request:
                is_active = request.get('is_active')
                del request['is_active']
            vr = product_validation.validate(request)
            if vr.get('success', False) is False:
                request_data['response']= ws_response(BAD_CODE, vr.get("error"), {})
            else :
                product_name = request.get('product_name')
                short_description = request.get('short_description')
                mrp = request.get('mrp')
                if product_already_exists(product_name, None):
                    request_data['response']=ws_response(BAD_CODE, messages.PRODUCT_ALREADY_EXIST, {})
                else:
                    product = Product(
                        id=uuid.uuid4(),
                        product_name=product_name,
                        short_description=short_description,
                        product_image=product_image,
                        is_active=is_active,
                        mrp=mrp,
                        author=user_id
                        )
                    product.save()
                    request_data['response']=ws_response(OK_CODE, messages.PRODUCT_ADDED_SUCCESS, product_dict(product))
        except Exception as e:
            request_data['response']=ws_response(BAD_CODE, str(e), {})
        return request_data


    def product_edit(self, request_data, user_id, user):
        request = False
        if "request" in request_data:
            request = request_data.get("request")
        try:
            product_id = request.get('product_id')
            del request['product_id']
            if 'is_active' in request:
                is_active = request.get('is_active')
                del request['is_active']
            vr = product_validation.validate(request)
            if vr.get('success', False) is False:
                request_data['response']= ws_response(BAD_CODE, vr.get("error"), {})
            else :
                product_name = request.get('product_name')
                short_description = request.get('short_description')
                product_image = request.get('product_image')
                mrp = request.get('mrp')
                if product_already_exists(product_name, product_id):
                    request_data['response']=ws_response(BAD_CODE, messages.PRODUCT_ALREADY_EXIST, {})
                else:
                    try:
                        product = Product.objects.get(id=uuid.UUID(product_id).hex)
                        product.product_name = product_name
                        product.short_description = short_description
                        product.product_image = product_image
                        product.mrp = mrp
                        product.is_active = is_active
                        product.author = user_id
                        product.save()
                        request_data['response']=ws_response(OK_CODE, messages.PRODUCT_UPDATED_SUCCESS, product_dict(product))
                    except Product.DoesNotExist:
                        request_data['response']=ws_response(BAD_CODE, messages.PRODUCT_NOT_FOUND, {})
        except Exception as e:
            request_data['response']=ws_response(BAD_CODE, str(e), {})
        return request_data


    def product_list(self, request_data, user_id, user):
        """
        Product list

        Args:
            status (bool): status type
            limit (str): limit per page
            page_no (str): page no
            search (str): search field

        Returns:
            array
        """
        product_list = []
        request = False
        if "request" in request_data:
            request = request_data.get("request")
        try:
            order_by = "-updated_at"
            order_by_list=['updated_at','-updated_at','product_name','-product_name','sku','-sku','mrp','-mrp','franchise_rate','-franchise_rate','is_active','-is_active']
            page_no = request.get("page_no")
            limit = request.get("limit")
            status = request.get("status")
            search = request.get("search")
            if 'order_by' in request:
                order_by_tmp = request.get("order_by")
                if order_by_tmp in order_by_list:
                    order_by = order_by_tmp
            data = pagination_validation(page_no, limit)
            if data:
                products = Product.objects.exclude(deleted_at__isnull=False).order_by(order_by)
                if status == True or status == False:
                    products = products.filter(is_active=status)
                if search :
                    search_query = Q(product_name__icontains=search) | Q(product_code__icontains=search) | Q(sku__icontains=search) | Q(hsn_code__icontains=search)
                    products = products.filter(search_query)
                counts = products.count()
                products = products[data["offset"]:data["page_result"]]
                if products:
                    for product in products:
                        if product:
                            product_list.append(product_dict(product))
                    paginated_res = {'pagination' : get_paginated_response(page_no, limit, counts), 'data' : product_list}
                    request_data['response']= ws_response(OK_CODE, messages.PRODUCT_FOUND, paginated_res)
                else:
                    request_data['response']= ws_response(BAD_CODE, messages.PRODUCT_NOT_FOUND, {})
            else:
                request_data['response']= ws_response(BAD_CODE, messages.PRODUCT_NOT_FOUND, {})
        except Exception as e:
            request_data['response']= ws_response(BAD_CODE, str(e), {})
        return request_data