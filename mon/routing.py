from django.urls import path, include
from monitoring.consumers import MonitoringConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({

    'websocket': AllowedHostsOriginValidator(
			URLRouter([
    			path("monitoring/", MonitoringConsumer) 
			]),
		),
	})