# Root Routing Configuration for Channels.
# It is similar to a Django URLconf in that it tells Channels
# what code to run
# when an HTTP request is received by the Channels server.

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import chat.routing

# ProtocolTypeRouter checks if it is a WebSocket connection
# AuthMiddlewareStack populates the connection’s scope
# with a reference to the currently authenticated user.
# URLRouter examines the HTTP path of the connection
# to route it to a particular consumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})