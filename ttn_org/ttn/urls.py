from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView, RedirectView

APP = 'ttn/'

urlpatterns = [
    # Examples:
    # url(r'^$', 'ttn_org.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Main website
    url(r'^$', TemplateView.as_view(template_name=APP+'index.html'),
        name='index'),

    # Community pages
    url(r'^c/(?P<slug>[0-9a-zA-Z_-]+)$',
        views.CommunityView.as_view(template_name=APP+'community/index.html'),
        name='community'),
    url(r'^start-a-community/(?P<search>[0-9a-zA-Z_-]+)?$',
        TemplateView.as_view(template_name=APP+'community/start-a-community.html'),
        name='new-community'),

    # Special pages
    url(r'^landing/kickstarter$',
        TemplateView.as_view(template_name=APP+'landing/kickstarter.html'),
        name='kickstarter'),
]
