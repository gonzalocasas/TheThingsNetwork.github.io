from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
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
    url(r'^accounts/password/reset/', auth_views.password_reset,
        {'template_name': 'registration/password_reset.html',
         'post_reset_redirect': reverse_lazy('password_reset_sent')},
        name='password_reset'),
    url(r'^accounts/password/reset/done', auth_views.password_reset_done,
        {'template_name': 'registration/password_reset_sent.html'},
        name='password_reset_sent'),
#views.PasswordResetView.as_view(
#        template_name='registration/password_reset_form.html'), name='password_reset'),
    url(r'^accounts/profile/', TemplateView.as_view(
        template_name='registration/profile.html'), name='profile'),
    # TODO: look at django-allauth
    # (r'', include('allauth.urls')),

    # API
    url(r'^api/$', RedirectView.as_view(url='v0/', permanent=False)),
    url(r'^api/v0/', include('api.urls', namespace='api'), name='api_root'),

    # special
    url(r'^robots.txt', TemplateView.as_view(template_name='robots.txt')),

]
