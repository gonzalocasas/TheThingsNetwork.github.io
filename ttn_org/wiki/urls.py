from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from . import views
from django.views.generic import TemplateView, RedirectView

APP = 'wiki/'
APPNS = 'wiki:'

urlpatterns = [

    url(r'^(?P<slug>[a-zA-Z0-9-_\/]+)$',
        views.PageView.as_view(template_name=APP+'page.html'),
        name='page'),

]

