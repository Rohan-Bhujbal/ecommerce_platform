import uuid
from order import messages
from order.models import Order
from app.globals import BAD_CODE, OK_CODE
from app.helper import pagination_validation, get_paginated_response, ws_response
from order.dict import order_dict
from product.helper import get_product_by_id


class OrderController:

    def order_add(self, request_data, user_id, user):
        request = False
        if "request" in request_data:
            request = request_data.get("request")
        try:
            total_qty = request.get('total_qty')
            product_id = request.get('product_id')         
            product = get_product_by_id(product_id)
            total = int(product.mrp) * int(total_qty)
            order = Order(
                id=uuid.uuid4(),
                total=total,
                qty=total_qty,
                product_id=product_id,
                user_id=user_id,
                )
            order.save()
            request_data['response']=ws_response(OK_CODE, messages.ORDER_ADDED_SUCCESS, order_dict(order))
        except Exception as e:
            request_data['response']=ws_response(BAD_CODE, str(e), {})
        return request_data


    def order_list(self, request_data, user_id, user):
        """
        Order list

        Args:
            status (str): status type
            limit (str): limit per page
            page_no (str): page no
            search (str): search field

        Returns:
            array
        """
        order_list = []
        request = False
        if "request" in request_data:
            request = request_data.get("request")
        try:
            page_no = request.get("page_no")
            limit = request.get("limit")
            data = pagination_validation(page_no, limit)
            if data:
                orders = Order.objects.exclude(deleted_at__isnull=False)
                counts = orders.count()
                orders = orders[data["offset"]:data["page_result"]]
                if orders:
                    for order in orders:
                        if order:
                            order_list.append(order_dict(order))
                    paginated_res = {'pagination' : get_paginated_response(page_no, limit, counts), 'data' : order_list}
                    request_data['response']= ws_response(OK_CODE, messages.ORDER_FOUND, paginated_res)
                else:
                    request_data['response']= ws_response(BAD_CODE, messages.ORDER_NOT_FOUND, {})
            else:
                request_data['response']= ws_response(BAD_CODE, messages.ORDER_NOT_FOUND, {})
        except Exception as e:
            request_data['response']= ws_response(BAD_CODE, str(e), {})
        return request_data