from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import Http404
from django.db import models
import requests
import html
import re
import json
import math
import os

from .views import JsonView
from .models import Community, Post, Gateway, InitiatorSubmission, Feed
from .forms import SettingsForm, PostForm


class KickstarterScraperView(JsonView):
    URL = "https://www.kickstarter.com/projects/419277966/the-things-network"

    def get(self, request, **kwargs):
        r = requests.get(self.URL).text
        search = re.search('window.current_project = "([^"]+)"', r)
        data = {}
        if search:
            data_str = search.group(1)
            data_str = html.unescape(data_str)
            data = json.loads(data_str)

        context = self.get_context_data(**kwargs)
        context['data'] = data
        return self.render_to_response(context)


