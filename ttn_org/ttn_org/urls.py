from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ttn_org.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # apps
    url(r'', include('ttn.urls', namespace='ttn')),

    # wiki
    url(r'^wiki/', include('waliki.urls')),

    # account
    #url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # TODO: look at django-allauth
    # (r'', include('allauth.urls')),

]
