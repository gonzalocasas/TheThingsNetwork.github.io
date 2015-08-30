from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import Http404

from .models import Community


class CommunityView(TemplateView):

    def get(self, request, slug, **kwargs):
        c = Community.objects.filter(slug=slug)
        if not c:
            return redirect('ttn:new-community', search=slug)
        context = self.get_context_data(**kwargs)
        context['community'] = c[0]
        return self.render_to_response(context)

