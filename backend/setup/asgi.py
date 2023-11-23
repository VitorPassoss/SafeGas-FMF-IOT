import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import socket_handler.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            socket_handler.routing.websocket_urlpatterns
        )
    )
})