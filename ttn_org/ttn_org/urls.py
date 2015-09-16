from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView, RedirectView
from ttn import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ttn_org.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # apps
    url(r'', include('ttn.urls', namespace='ttn')),

    # wiki
    url(r'^wiki/', include('waliki.urls')),
    url(r'^wiki2/', include('wiki.urls')),

    # account
    #url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/', views.SignupView.as_view(
        template_name='registration/signup.html'), name='signup'),
    url(r'^accounts/profile/', TemplateView.as_view(
        template_name='registration/profile.html'), name='profile'),
    # TODO: look at django-allauth
    # (r'', include('allauth.urls')),

    # API
    url(r'^api/v0/', include('api.urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
