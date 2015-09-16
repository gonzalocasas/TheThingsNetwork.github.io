from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from . import views
from django.views.generic import TemplateView, RedirectView

APP = 'api/'
APPNS = 'api:'

urlpatterns = [

    url(r'^(?P<slug>[a-zA-Z0-9-_\/]+)$',
        TemplateView.as_view(template_name=APP+'page.html'),
        name='page'),

]


