import jwt
import json
import uuid
import datetime
import httpagentparser
from django.conf import settings
from user.models import User, UserToken
from django.forms.models import model_to_dict
from channels.db import database_sync_to_async
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


def user_pass_encode(raw_password):
    return make_password(raw_password)


def check_user_pass(raw_password, hashed_password):
    is_valid = False
    print(raw_password)
    print("raw_password")
    print(hashed_password)
    if check_password(raw_password, hashed_password):
        is_valid = True
    return is_valid


def get_user_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def detect_browser(request):
    user_agent = request.META['HTTP_USER_AGENT']
    browser = httpagentparser.simple_detect(user_agent)
    return browser


def get_user_dict(user):
    user_dict = {}
    try:
        user_dict = model_to_dict(user)
        user_dict["id"] = str(user.id)
        user_dict["author"] = str(user.author)
        user_dict["created_at"] = str(user.created_at)
        user_dict["updated_at"] = str(user.updated_at)
        user_dict["deleted_at"] = str(user.deleted_at)
        del user_dict['password']
    except Exception:
        user_dict = {}
    return user_dict


def generate_access_token(user, request, device_type, device_id):
    user_agent = detect_browser(request)
    user_token = UserToken(
        id=uuid.uuid4(),
        user_id=user.id,
        user_ip=get_user_ip(request),
        user_agent=user_agent,
        device_type=device_type,
        device_id=device_id,
    )
    user_token.save()
    if user_token:
        access_token = user_access_token(user_token)
        return access_token



def user_access_token(user_token):
    access_token_payload = {
            "token_id": str(user_token.id),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=365, minutes=5),
            "iat": datetime.datetime.utcnow(),
        }
    access_token = jwt.encode(
            access_token_payload, settings.SECRET_KEY, algorithm="HS256"
        )
    return access_token



def get_user_id_by_token(token_id):
    user_id = ""
    try:
        user_token = UserToken.objects.get(id=uuid.UUID(token_id).hex, is_active=True)
        if user_token:
            user_id = str(user_token.user_id)
    except Exception:
        user_id = ""
    return user_id


def get_user(user_id):
    res = {}
    try:
        user = User.objects.exclude(deleted_at__isnull=False).get(id=user_id)
        if user:
            res = user
    except Exception as e:
        print(e)
        res = {}
    return res



def user_logout(token_id):
    user_dict = {}
    try:
        user_token = UserToken.objects.get(id=uuid.UUID(token_id).hex, is_active=True)
        if user_token:
            user_token.is_active = False
            user_token.save()
            user_dict["token_id"] = token_id     
            user_dict["device_type"] = user_token.device_type
            user_dict["is_active"] = user_token.is_active
    except Exception:
        user_dict = {}
    return user_dict



def get_user_by_id(user_id):
    user_dict = {}
    try:
        user = User.objects.filter(id=uuid.UUID(user_id).hex).first()
        if user:
            user_dict = get_user_dict(user)
    except Exception:
        user_dict = {}
    return user_dict



@database_sync_to_async
def get_user_id_by_token_id(token_id):
    return get_user_id_by_token(token_id)



@database_sync_to_async
def get_user_by_user_id(user_id):
    return get_user_by_id(user_id)



def auth_token(request):
    authorization_header = request.headers.get("Authorization")
    if not authorization_header:
        return None
    try:
        access_token = authorization_header.split(" ")[1]
        payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=["HS256"])
        token_id = payload["token_id"]
    except Exception:
        token_id = ""
    return token_id

def is_login(request):
    user_id = None
    if 'user_id' in request.session:
        user_id = request.session['user_id']
    else:
        token_id = auth_token(request)
        if token_id :
            user_id = get_user_id_by_token(token_id)
    if user_id != None and user_id != "":
        return True
    else:
        return False