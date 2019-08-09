from django.urls import path, include
from dashboard.consumers import DashBoardConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({

    'websocket': AllowedHostsOriginValidator(
			URLRouter([
    			path("dashboard/", DashBoardConsumer) 
			]),
		),
	})