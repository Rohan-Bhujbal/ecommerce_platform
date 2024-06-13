import json
import datetime
from uuid import UUID
from user.models import UserToken
from user.auth import get_user
from app.helper import ws_response
from django.http import JsonResponse
from asgiref.sync import async_to_sync
from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from app.globals import VAR_SINGLE, WITHOUT_LOGIN_URLS, USER_IS_NOT_AUTHORIZED, VAR_URLS, AUTH_CODE

# Add controller for each ws
from user.user import UserController


def user_authentication(user_id, token_id, url):
    res = False
    if (user_id != "") or (token_id != ""):
        if (user_id == "guest") or (token_id == "guest"):
            if url in WITHOUT_LOGIN_URLS:
                res = True
        else:
            user = get_user(user_id)
            if user :
                if user.user_type == "admin" :
                    res = True
                else:
                    if user.user_type == "staff" :
                        user_permission = user.permissions
                        if user_permission is not None:
                            if url in user_permission.split(","):
                                res = True
    return res


class SchemeConsumer(SyncConsumer):


    def websocket_connect(self, event):
        user_id = self.scope["user_id"]
        token_id = self.scope["token_id"]
        if user_id != "":
            self.send({"type": "websocket.accept"})
            self.room_name = str(user_id)
            async_to_sync(self.channel_layer.group_add)(
                self.room_name, self.channel_name
                    )
            self.channel_layer.group_add(self.room_name, self.channel_name)
            if token_id != "guest":
                UserToken.objects.filter(id=UUID(str(token_id)).hex).update(updated_at=datetime.datetime.now())
        else:
            self.send({"type": "websocket.accept"})
            request_data = {"transmit":"single", "url":"unauthorized"}
            get_response = JsonResponse(request_data, safe=False)
            response_data = (get_response.content).decode()
            self.send({"type": "websocket.send", "text":response_data})
            self.send({"type": "websocket.close"})


    def websocket_receive(self, event):
        if self.scope["user_id"] == "":
            self.send({"type": "websocket.close"})
        else:
            try:
                request_data = json.loads(event["text"])  
            except json.JSONDecodeError:
                request_data = {}
            request_data["user_id"] = self.scope["user_id"]
            token_id = self.scope["token_id"]
            if token_id != "guest":
                user_token_count = UserToken.objects.filter(id=UUID(str(token_id)).hex, is_active = True).count()
                if user_token_count == 0:
                    self.send({"type": "websocket.close"})
            if 'transmit' in request_data:
                transmit = request_data.get("transmit")
            else :
                transmit = None
            if 'url' in request_data:
                url = request_data.get("url")
            else :
                url = None
            if url in WITHOUT_LOGIN_URLS:
                transmit = VAR_SINGLE
            # User
            if not user_authentication(self.scope["user_id"], self.scope["token_id"], url):
                request_data["response"] = ws_response(AUTH_CODE, USER_IS_NOT_AUTHORIZED, {})
            else:
                # Response
                if url != None :
                    user_id = self.scope["user_id"]
                    if url in VAR_URLS :
                        function_name = VAR_URLS[url]['function']
                        class_name = VAR_URLS[url]['class']
                        class_obj = globals()[class_name]()
                        request_data = getattr(class_obj, function_name)(request_data, user_id)

            get_response = JsonResponse(request_data, safe=False)
            response_data = (get_response.content).decode()
            if transmit == "broadcast":
                async_to_sync(self.channel_layer.group_send)(
                    self.room_name, {"type": "websocket.reply", "text": response_data}
                )
            else:
                self.send({"type": "websocket.send", "text": response_data})


    def websocket_reply(self, event):
        self.send({"type": "websocket.send", "text": event.get("text")})


    def websocket_disconnect(self, event):
        if self.scope["user_id"] != "":
            async_to_sync(self.channel_layer.group_discard)(
                self.room_name, self.channel_name
            )
        raise StopConsumer()