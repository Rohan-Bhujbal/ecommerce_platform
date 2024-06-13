import jwt
import uuid
from user.models import User
from django.conf import settings
from rest_framework import exceptions
from channels.middleware import BaseMiddleware
from rest_framework.authentication import BaseAuthentication
from user.auth import get_user_id_by_token, get_user_id_by_token_id



class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None
        try:
            access_token = authorization_header.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])
            token_id = payload['token_id']
            user_id = get_user_id_by_token(token_id)
        except jwt.exceptions.InvalidSignatureError:
            raise exceptions.AuthenticationFailed('Invalid token.')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token expired.')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing.')
        if user_id == "":
            raise exceptions.AuthenticationFailed('Token expired.')
        user = User.objects.exclude(deleted_at__isnull=False).filter(id=uuid.UUID(user_id).hex).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found.')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('User is inactive.')
        user.is_authenticated = True
        return (user, None)


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        try:
            access_token = scope['path'].replace("/ws/", "")
            if access_token[:-1] == "guest":
                scope['token_id'] = "guest"
                scope['user_id'] = "guest"           
            else:
                payload = jwt.decode(
                    access_token[:-1], settings.SECRET_KEY, algorithms=['HS256'])
                token_id = payload['token_id']
                scope['token_id'] = token_id
                scope['user_id'] = await get_user_id_by_token_id(token_id)
        except ValueError:
            scope['token_id'] = ""
            scope['user_id'] = ""
        except Exception:
            scope['token_id'] = ""
            scope['user_id'] = ""
        return await super().__call__(scope, receive, send)
