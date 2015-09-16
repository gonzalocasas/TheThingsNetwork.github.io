from django.shortcuts import render
from django.views.generic import TemplateView


class PageView(TemplateView):

    def get(self, request, slug, **kwargs):
        context = self.get_context_data(**kwargs)
        context['slug'] = slug
        return self.render_to_response(context)

