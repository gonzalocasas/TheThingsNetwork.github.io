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

from . import utils
from .views import JsonView
from .models import Community, Post, Gateway, InitiatorSubmission, Feed, key_lookup, key_save
from .forms import SettingsForm, PostForm


class KickstarterScraperView(JsonView):
    URL = "https://www.kickstarter.com/projects/419277966/the-things-network"
    # NOTE: includes API call (how long does this token work?)
    # https://api.kickstarter.com/v1/projects/142224319?signature=1446030403.620ac4cbf2dd262d8a0bb2c36c48ec1dcbba540e

    def get(self, request, **kwargs):
        r = requests.get(self.URL).text
        search = re.search('window.current_project = "([^"]+)"', r)
        data = {}
        if search:
            ks_data_str = search.group(1)
            ks_data_str = html.unescape(ks_data_str)
            ks_data = json.loads(ks_data_str)
            for key in ['backers_count', 'pledged', 'goal']:
                data[key] = ks_data.get(key)
            data['pledges'] = []
            for reward in ks_data.get('rewards', []):
                data['pledges'].append({
                    'description': reward.get('description', ''),
                    'backers_count': reward.get('backers_count', 0)
                })

        # send events, update db
        ks_key = 'kickstarter_data'
        data_prev = key_lookup(ks_key, {})
        percentage = data.get('pledged') / data.get('goal') * 100
        message = "*New Kickstarter Pledge*!\nTotal euros pledged: *{}* ({:.1f}%) by {} backers".format(
            data.get('pledged', '???'), percentage, data.get('backers_count', '???'))
        print(message)
        if data_prev.get('backers_count', 0) < data.get('backers_count', 0):
            percentage = data.get('pledged') / data.get('goal') * 100
            message = "*New Kickstarter Pledge*!\nTotal euros pledged: *{}* ({.1f}%) by {} backers".format(
                data.get('pledged', '???'), percentage, data.get('backers_count', '???'))
            print(message)
            utils.send_slack(text=message)
        key_save(ks_key, data)

        # return JSON
        context = self.get_context_data(**kwargs)
        context['data'] = data
        return self.render_to_response(context)


