from django.conf.urls import include, url
#from django.core.urlresolvers import reverse_lazy
#from django.contrib.auth.decorators import login_required
#from django.views.generic import TemplateView, RedirectView
from . import views
from rest_framework import routers, serializers, viewsets

APP = 'api/'
APPNS = 'api:'



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#router.register(r'gateways', views.GatewayView)


urlpatterns = [

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^', include(router.urls), name='api'),
    url(r'^/?$', views.IndexView.as_view(), name='api'),

    # TODO: get in router / root overview
    url(r'^gateways/$', views.GatewayView.as_view(), name='gateways'),
    url(r'^gateways/(?P<eui>[0-9a-zA-Z]+)/$', views.GatewayView.as_view(),
        name='gateway'),
    url(r'^nodes/$', views.NodeView.as_view(), name='nodes'),
    url(r'^nodes/(?P<node_eui>[0-9a-zA-Z]+)/$', views.NodeView.as_view(),
        name='node'),

]


