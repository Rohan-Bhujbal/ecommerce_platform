from django.urls import path
from core import consumers

websocket_urlpatterns = [
    path('ws/<str:access_token>/', consumers.SchemeConsumer.as_asgi()),
]