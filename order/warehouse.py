import uuid
from order import messages
from app.globals import BAD_CODE, OK_CODE
from app.helper import ws_response
from order.helper import order_by_id, order_add_log, revert_franchise_debit, order_add_count
from order.dict import order_dict
from order.validations import (
    cancelled_validation
)
from django.utils import timezone
from user.auth import get_user
from django.db import transaction


class OrderWarehouseController:


    def wh_cancelled(self, request_data, user_id, user):
        request = False
        if "request" in request_data:
            request = request_data.get("request")
        try:
            with transaction.atomic():
                vr = cancelled_validation.validate(request)
                if vr.get('success', False) is False:
                    request_data['response']= ws_response(BAD_CODE, vr.get("error"), {})
                else :
                    order_id = request.get('order_id')
                    order_status = request.get('order_status')
                    if order_id: 
                        is_valid = False
                        order = order_by_id(order_id)
                        if order_status == "REJECTED" and  order.order_status == "WH_PENDING" and str(user.related_id) == str(order.warehouse_id) :
                            cancel_reason = request.get('cancel_reason')
                            if cancel_reason :
                                is_valid = True
                                order.cancel_reason = cancel_reason
                                order.cancel_stage = order.order_status 
                                order.cancel_at = timezone.now()
                                order.cancel_type = "MANUAL"
                                order.order_status = order_status
                            else :
                                request_data['response']=ws_response(BAD_CODE, messages.PLEASE_ENTER_CANCEL_REASON, {})
                            if is_valid == True :
                                order.author = user_id
                                order.save()
                                revert_franchise_debit(order,user_id)
                                order_add_log(order,user_id,user_id)
                                order_add_count(order)
                                request_data['response']=ws_response(OK_CODE, messages.ORDER_CANCELLED_SUCCESS, order_dict(order))
                        else :
                            request_data['response']=ws_response(BAD_CODE, messages.ORDER_NOT_FOUND, {})
        except Exception as e:
            request_data['response']=ws_response(BAD_CODE, str(e), {})
        return request_data


    def wh_order_approval(self, request_data, user_id, user):
        request = False
        if "request" in request_data:
            request = request_data.get("request")
        try:
            with transaction.atomic():
                request_data['response']=ws_response(BAD_CODE, messages.ORDER_NOT_FOUND, {})
                order_id = request.get('order_id')
                if order_id:
                    order = order_by_id(order_id)
                    if order.order_status == "WH_PENDING" and str(user.related_id) == str(order.warehouse_id) :
                        order.order_status = "WH_APPROVED"
                        order.author = user_id
                        order.save()
                        order_add_log(order,user_id,user_id)
                        request_data['response']=ws_response(OK_CODE, messages.ORDER_APPROVAL_SUCCESS, order_dict(order))
        except Exception as e:
            request_data['response']=ws_response(BAD_CODE, str(e), {})
        return request_data