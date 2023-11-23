from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/iot', consumers.IotConsumer.as_asgi()),
]