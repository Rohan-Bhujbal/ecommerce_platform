from user.validations import (
    user_validation,
)
import uuid
from app.helper import ws_response
from user import messages
from user.models import User
from app.globals import BAD_CODE, OK_CODE, USER_TYPE
from app.helper import pagination_validation, get_paginated_response
from user.helper import user_already_exists, user_pass_encode, user_mobile_already_exists
from app.helper import pass_validation
from user.auth import get_user_dict


class UserController:


    def user_add(self, request_data, user_id):
        request = False
        if "request" in request_data:
            request = request_data.get("request")
        try:
            vr = user_validation.validate(request)
            if vr.get('success', False) is False:
                request_data['response']= ws_response(BAD_CODE, vr.get("error"), {})
            else :
                full_name = request.get('full_name')
                email = request.get('email')
                mobile = request.get('mobile')
                address = request.get('address')
                password = request.get('password')
                user_type = request.get('user_type')
                permissions = request.get('permissions')
                is_active = request.get('is_active')
                related_id = request.get('related_id')
                if user_type not in USER_TYPE:
                    user_type = 'user'
                if user_already_exists(email, None):
                    request_data['response']=ws_response(BAD_CODE, messages.EMAIL_ALREADY_REGISTERED_TRY_LOGIN, {})
                elif user_mobile_already_exists(mobile, None):
                    request_data['response']=ws_response(BAD_CODE, messages.MOBILE_ALREADY_REGISTERED_TRY_LOGIN, {})
                elif not pass_validation(password):
                    request_data['response']=ws_response(BAD_CODE, messages.P_CRITERIA_NOT_MATCH, {})
                else:
                    encode_pass = user_pass_encode(password)
                    user_code = 'UM001'
                    latest_object = User.objects.filter(user_code__isnull=False).order_by('-user_code').first()
                    if latest_object.user_code :
                        last_value = int(latest_object.user_code[2:])
                        user_code = f'UM{last_value + 1:03}'

                    user = User(
                        id=uuid.uuid4(),
                        full_name=full_name,
                        email=email, 
                        mobile=mobile,
                        address=address,
                        password=encode_pass,
                        user_type=user_type,
                        permissions=permissions,
                        is_active=is_active,
                        user_code=user_code,
                        related_id=related_id,
                        author=user_id
                        )
                    user.save()
                    request_data['response']=ws_response(OK_CODE, messages.USER_ADDED_SUCCESS, get_user_dict(user))
        except Exception as e:
            request_data['response']=ws_response(BAD_CODE, str(e), {})
        return request_data


    def user_edit(self, request_data, user_id):
        
        request = False
        if "request" in request_data:
            request = request_data.get("request")
        try:
            userid = request.get('userid')
            del request['userid']
            request['password'] = "password"
            vr = user_validation.validate(request)
            if vr.get('success', False) is False:
                request_data['response']= ws_response(BAD_CODE, vr.get("error"), {})
            else :
                full_name = request.get('full_name')
                email = request.get('email')
                mobile = request.get('mobile')
                address = request.get('address')
                user_type = request.get('user_type')
                permissions = request.get('permissions')
                is_active = request.get('is_active')
                related_id = request.get('related_id')
                if user_already_exists(email, userid):
                    request_data['response']=ws_response(BAD_CODE, messages.EMAIL_ALREADY_REGISTERED_TRY_LOGIN, {})
                elif user_mobile_already_exists(mobile, userid):
                    request_data['response']=ws_response(BAD_CODE, messages.MOBILE_ALREADY_REGISTERED_TRY_LOGIN, {})
                else:
                    try:
                        user = User.objects.get(id=uuid.UUID(userid).hex)
                        user.full_name=full_name
                        user.email=email
                        user.mobile=mobile
                        user.address=address
                        user.user_type=user_type
                        user.permissions=permissions
                        user.is_active=is_active
                        user.author=user_id
                        user.related_id=related_id
                        user.save()
                        request_data['response']=ws_response(OK_CODE, messages.USER_UPDATE_SUCCESS, get_user_dict(user))
                    except User.DoesNotExist:
                        request_data['response']=ws_response(BAD_CODE, messages.USER_UPDATE_UNSUCCESS, {})
        except Exception as e:
            request_data['response']=ws_response(BAD_CODE, str(e), {})
        return request_data


    def user_list(self, request_data, user_id,user):
        """
        User list

        Args:
            status (bool): status type
            limit (str): limit per page
            page_no (str): page no
            search (str): search field

        Returns:
            array
        """
        user_list = []
        request = False
        if "request" in request_data:
            request = request_data.get("request")
        try:
            order_by = "-updated_at"
            order_by_list=['updated_at','-updated_at','email','-email','mobile','-mobile','full_name','-full_name','user_type','-user_type','is_active','-is_active']
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
                users = User.objects.exclude(deleted_at__isnull=False).order_by(order_by)
                if status == True or status == False:
                    users = users.filter(is_active=status)
                if search :
                    users = users.filter(email__iregex=search)
                counts = users.count()
                users = users[data["offset"]:data["page_result"]]
                if users:
                    for user in users:
                        if user:
                            user_list.append(get_user_dict(user))
                    paginated_res = {'pagination' : get_paginated_response(page_no, limit, counts), 'data' : user_list}
                    request_data['response']= ws_response(OK_CODE, messages.USER_FOUND, paginated_res)
                else:
                    request_data['response']= ws_response(BAD_CODE, messages.USER_NOT_FOUND, {})
            else:
                request_data['response']= ws_response(BAD_CODE, messages.USER_NOT_FOUND, {})
        except Exception as e:
            request_data['response']= ws_response(BAD_CODE, str(e), {})
        return request_data