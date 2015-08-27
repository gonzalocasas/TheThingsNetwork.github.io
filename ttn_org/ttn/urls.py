from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView, RedirectView

APP = 'ttn'

urlpatterns = [
    # Examples:
    # url(r'^$', 'ttn_org.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name=APP+'/index.html'),
        name='index'),
    url(r'^landing/kickstarter$', TemplateView.as_view(template_name=APP+'/landing/kickstarter.html'),
        name='kickstarter'),
]
