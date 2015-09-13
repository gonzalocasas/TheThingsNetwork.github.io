from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import Http404
from django.db import models

from .models import Community, Post, Gateway, InitiatorSubmission
from .forms import SettingsForm


class IndexView(TemplateView):

    def get(self, request, **kwargs):
        c = Community.objects.filter(published=True) \
                             .annotate(gateways_count=models.Count('gateways')) \
                             .order_by('-gateways_count')
        context = self.get_context_data(**kwargs)
        context['communities'] = c
        return self.render_to_response(context)


class CommunityView(TemplateView):

    def get(self, request, slug, **kwargs):
        community = self._get_community(slug=slug)
        permissions = self._get_permissions(request.user, community)
        context = self.get_context_data(**kwargs)
        context['community'] = community
        context['permissions'] = permissions
        return self.render_to_response(context)

    def _get_community(self, slug):
        c = Community.objects.filter(slug=slug)
        if not c:
            return redirect('ttn:new-community', search=slug)
        return c[0]

    def _get_permissions(self, user, community=None):
        p = []
        if user.is_staff or (community and user in community.members.all()):
            p.append('contributor')
        if user.is_staff or (community and user in community.leaders.all()):
            p.append('admin')
        return p
        

class StartCommunityView(TemplateView):
    
    def get(self, request, search, **kwargs):
        context = self.get_context_data(**kwargs)
        context['search'] = search or ""
        return self.render_to_response(context)

    def post(self, request, **kwargs):
        submission = InitiatorSubmission()
        for field in ['name', 'email', 'url', 'skills', 'area',
                      'contributors', 'plan', 'helping']:
            setattr(submission, field, request.POST.get(field, ''))
        submission.save()
        return redirect('ttn:new-community-thanks')


class OverviewView(TemplateView):

    def get(self, request, **kwargs):
        cs = Community.objects.all()
        gws = Gateway.objects.all()
        context = self.get_context_data(**kwargs)
        context['communities'] = cs
        context['gateways'] = gws
        return self.render_to_response(context)


class PostView(CommunityView):

    def get(self, request, slug, pk, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = self.get_context_data(**kwargs)
        context['community'] = self._get_community(slug=slug)
        context['post'] = post
        return self.render_to_response(context)


class SettingsView(CommunityView):

    def get(self, request, slug, **kwargs):
        community = self._get_community(slug=slug)
        permissions = self._get_permissions(request.user, community)
        if 'admin' not in permissions:
            return redirect('ttn:community', slug=slug) # no access
        form = SettingsForm(instance=community)
        context = self.get_context_data(**kwargs)
        context['community'] = self._get_community(slug=slug)
        context['permissions'] = permissions
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, slug, **kwargs):
        community = self._get_community(slug=slug)
        permissions = self._get_permissions(request.user, community)
        if 'admin' in permissions:
            settings = SettingsForm(request.POST, instance=community)
            settings.save()
        return redirect('ttn:community', slug=slug)

