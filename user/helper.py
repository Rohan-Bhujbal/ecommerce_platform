import uuid
from user import messages
from app.helper import ws_response
from django.forms.models import model_to_dict
from user.models import User, UserToken
from user.auth import generate_access_token, get_user_dict, get_user, check_user_pass, user_pass_encode
from app.globals import BAD_CODE, OK_CODE, VAR_MINUTES
import re
from datetime import datetime, timedelta
from app.messages import SOMETHING_WENT_WRONG


def user_already_exists(email, user_id):
    """
    Method: Check if a user with the given email already exists in the database.

    Args:
        email (str): User email.

    Returns:
        True if the same user email already present in the database, else False.
    """
    try:
        if user_id:
            return User.objects.filter(email=email).exclude(id=uuid.UUID(user_id).hex).exists()
        else:
            return User.objects.filter(email=email).exists()
    except Exception:
        return True


def user_mobile_already_exists(mobile, user_id):
    """
    Method: Check if a user with the given mobile already exists in the database.

    Args:
        mobile (str): User mobile.

    Returns:
        True if the same user mobile already present in the database, else False.
    """
    try:
        if user_id:
            return User.objects.filter(mobile=mobile).exclude(id=uuid.UUID(user_id).hex).exists()
        else:
            return User.objects.filter(mobile=mobile).exists()
    except Exception:
        return True


def get_login_user(user, request, device_type, device_id):
    """
    Method : Get Login User

    Args:
        request (self): request parameter
        user (object): query object
        device_type (str): web or android

    Returns:
        User object with access token
    """
    access_token = generate_access_token(user, request, device_type, device_id)
    user_dict = get_user_dict(user)
    return {
        "user": user_dict,
        "access_token": access_token,
        "device_id" : device_id
    }


def user_profile_update(user_id, full_name, old_pass, new_pass):
    """
    Method: User Profile Update

    Args:
        user_id (uuid): self user id
        username (str): user first name to update
        last_name (str): user last name update
        old_pass (str): user old password to change
        new_pass (str): user new password to set

    Returns:
        Updated user object
    """
    response = {}
    try:
        msg = messages.USER_UPDATE_SUCCESS
        user = get_user(user_id)
        
        if full_name:
            user.full_name = full_name
        if old_pass and new_pass:
            if old_pass != new_pass:
                is_verified = check_user_pass(old_pass, user.password)
                if is_verified:
                    encoded_pass = user_pass_encode(new_pass)
                    user.password = encoded_pass
                else:
                    return ws_response(BAD_CODE, messages.WRONG_PASS, {})
            else:
                return ws_response(BAD_CODE, messages.NEW_AND_OLD_P, {})

        if full_name or (old_pass and new_pass):
            user.save()
            user_dict = get_user_dict(user)
            response = ws_response(OK_CODE, msg, user_dict)
        else:
            response = ws_response(BAD_CODE, SOMETHING_WENT_WRONG, {})
    except Exception:
        response = ws_response(BAD_CODE, messages.USER_UPDATE_UNSUCCESS, {})
    return response



def get_active_token_list(user_id):
    user_token_dict = {}
    user_token_list = []
    try:
        user_tokens = UserToken.objects.filter(user_id=user_id, is_active=True).all().order_by("-created_at")[1:]
        if user_tokens:
            for user_token in user_tokens:
                user_token_dict = model_to_dict(user_token)
                user_token_dict['id'] = str(user_token.id)
                user_token_dict['created_at'] = str(user_token.created_at)
                user_token_dict['updated_at'] = str(user_token.updated_at)
                user_token_list.append(user_token_dict)
    except Exception:
        user_token_dict = {}
        user_token_list = []
    return user_token_list


def deactivate_token(user_id, id):
    user_token_dict = {}
    try:
        user_token = UserToken.objects.get(id=uuid.UUID(str(id)).hex, user_id=user_id, is_active=True)
        if user_token:
            user_token.is_active = False
            user_token.save()
            user_token_dict = model_to_dict(user_token)
            user_token_dict["id"] = str(user_token.id)
            user_token_dict["created_at"] = str(user_token.created_at)
            user_token_dict["updated_at"] = str(user_token.updated_at)
    except Exception:
        user_token_dict = {}
    return user_token_dict


def remove_html_tags(text):
    TAG_RE = re.compile(r"(<([^>]+)>)")
    return TAG_RE.sub("", text)


def get_response():
    res = {"msg": "", "data": [], "errors": []}
    return res


def session_timeout(user_qr_code):
    try:
        now = datetime.now().strftime("%H:%M:%S")
        created_at = user_qr_code.created_at.time().strftime("%H:%M:%S")
        final_time = (user_qr_code.created_at) + timedelta(minutes=VAR_MINUTES)
        delta = final_time.time().strftime("%H:%M:%S")
        
        now_time_obj = datetime.strptime(now, "%H:%M:%S")
        created_time_obj = datetime.strptime(created_at, "%H:%M:%S")
        delta_time_obj = datetime.strptime(delta, "%H:%M:%S")

        now_time = float((now_time_obj.strftime("%H:%M")).replace(':','.'))
        created_time = float((created_time_obj.strftime("%H:%M")).replace(':','.'))
        delta_time = float((delta_time_obj.strftime("%H:%M")).replace(':','.'))
        
        if (now_time < delta_time) and (now_time >= created_time) :
            return True
    except Exception:
        return False
    return False
