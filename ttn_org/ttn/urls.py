from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from . import views
from django.views.generic import TemplateView, RedirectView

APP = 'ttn/'
APPNS = 'ttn:'

urlpatterns = [
    # Examples:
    # url(r'^$', 'ttn_org.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Main website
    url(r'^$', views.IndexView.as_view(template_name=APP+'index.html'),
        name='index'),

    # Community pages
    url(r'^c/(?P<slug>[0-9a-zA-Z_-]+)/?$',
        views.CommunityView.as_view(template_name=APP+'community/index.html'),
        name='community'),
    url(r'^c/(?P<slug>[0-9a-zA-Z_-]+)/contact/?$',
        views.CommunityView.as_view(template_name=APP+'community/contact.html'),
        name='community-contact'),
    url(r'^c/(?P<slug>[0-9a-zA-Z_-]+)/post/(?P<pk>[0-9a-zA-Z_-]+)$',
        views.PostView.as_view(template_name=APP+'community/post.html'),
        name='community-post'),
    url(r'^start-a-community/(?P<search>[0-9a-zA-Z_-]+)?$',
        TemplateView.as_view(template_name=APP+'community/start-a-community.html'),
        name='new-community'),

    # Special pages
    url(r'^landing/kickstarter$',
        TemplateView.as_view(template_name=APP+'landing/kickstarter.html'),
        name='kickstarter'),
    url(r'^kickstarter-landing/kickstarter.html$',
        RedirectView.as_view(url=reverse_lazy(APPNS+'kickstarter'), permanent=True)),
]
