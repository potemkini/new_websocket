from django.urls import re_path, path
from chat.consumers import *

websocket_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),
]
