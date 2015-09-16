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


urlpatterns = [

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),

    url(r'^custom/', views.CustomView.as_view(), name='custom'),

]


