from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.db import models
import math
import os

from . import utils
from .models import Community, Post, Gateway, InitiatorSubmission, Feed
from .forms import SettingsForm, PostForm


class JsonView(TemplateView):
    template_name = 'ttn/json.html'

    def render_to_response(self, context, **kwargs):
        return JsonResponse(context['data'], **kwargs)


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
        if not community:
            return redirect('ttn:new-community', search=slug)
        permissions = self._get_permissions(request.user, community)
        context = self.get_context_data(**kwargs)
        context['community'] = community
        context['permissions'] = permissions
        return self.render_to_response(context)

    def _get_community(self, slug):
        c = Community.objects.filter(slug=slug)
        if not c:
            return False
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
        # notify
        message = "*Initiator submission* in _{}_ by {}".format(
            submission.area, submission.name)
        utils.send_slack(message)
        return redirect('ttn:new-community-thanks')


class MapView(TemplateView):

    def get(self, request, **kwargs):
        cs = Community.objects.all()
        gws = Gateway.objects.all()
        cskeys = ['lat', 'lon', 'scale', 'title', 'slug', 'image_url', 'published']
        cs_filtered = [{key: getattr(c, key) for key in cskeys} for c in cs]
        context = self.get_context_data(**kwargs)
        context['communities'] = cs_filtered
        context['gateways'] = gws
        return self.render_to_response(context)


class PostView(CommunityView):

    def get(self, request, slug, pk, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        community = self._get_community(slug=slug)
        permissions = self._get_permissions(request.user, community)
        if not community:
            return redirect('ttn:new-community', search=slug)
        context = self.get_context_data(**kwargs)
        context['community'] = community
        context['permissions'] = permissions
        context['post'] = post
        return self.render_to_response(context)


class PostEditView(PostView):

    def get(self, request, slug, pk, **kwargs):
        community = get_object_or_404(Community, slug=slug)
        post = Post.objects.filter(pk=pk)[0] if pk != 'new' else None
        form = PostForm(instance=post)
        permissions = self._get_permissions(request.user, community)
        context = self.get_context_data(**kwargs)
        context['community'] = community
        context['post'] = post
        context['permissions'] = permissions
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, slug, pk, **kwargs):
        community = get_object_or_404(Community, slug=slug)
        post = Post.objects.filter(pk=pk)[0] if pk != 'new' else None
        permissions = self._get_permissions(request.user, community)
        if 'admin' in permissions:
            new_post = PostForm(request.POST, instance=post)
            post = new_post.save(commit=False)
            if pk == 'new':
                post.author = request.user
                post.community = community
            post.save()
            if pk == 'new':
                # notify
                message = "*Community post added*\n{}".format(
                    request.build_absolute_uri(reverse(
                        'ttn:community-post', kwargs={'slug': slug, 'pk': post.pk})))
                utils.send_slack(message)
        return redirect('ttn:community-post', slug=slug, pk=post.pk)


class SettingsView(CommunityView):

    def get(self, request, slug, **kwargs):
        community = self._get_community(slug=slug)
        if not community:
            return redirect('ttn:new-community', search=slug)
        permissions = self._get_permissions(request.user, community)
        if 'admin' not in permissions:
            return redirect('ttn:community', slug=slug) # no access
        form = SettingsForm(instance=community)
        context = self.get_context_data(**kwargs)
        context['community'] = community
        context['permissions'] = permissions
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, slug, **kwargs):
        community = self._get_community(slug=slug)
        if not community:
            return redirect('ttn:new-community', search=slug)
        permissions = self._get_permissions(request.user, community)
        if 'admin' in permissions:
            new_settings = SettingsForm(request.POST, instance=community)
            settings = new_settings.save()
            # notify
            message = "*Community page updated* by {} {}\n{}".format(
                request.user.first_name, request.user.last_name,
                request.build_absolute_uri(reverse(
                    'ttn:community', kwargs={'slug': slug})))
            utils.send_slack(message)
        return redirect('ttn:community', slug=slug)


class FeedView(TemplateView):
    
    def get(self, request, **kwargs):
        activities = Feed.object.all()
        context = self.get_context_data(**kwargs)
        context['activities'] = activities
        return self.render_to_response(context)


## General non-TTN views
class SignupView(TemplateView):

    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        errors = []
        if not (first_name and last_name):
            errors.append("Please fill in your first and last name.")
        if not email or not '@' in email:
            errors.append("Please provide a valid email address.")
        if not username:
            username = first_name.lower().replace(' ', '_')
        if password1 != password2:
            errors.append("Passwords don't match.")
        if len(password1 or '') < 8:
            errors.append("Password too simple. Please use at least 8 characters.")
        if email:
            search_email = User.objects.filter(email=email)
            if search_email:
                errors.append("Email address already registered!")
        if username:
            search_username = User.objects.filter(username=username)
            if search_username:
                errors.append("Username already taken!")

        if errors:
            return self.get(request, errors=errors, first_name=first_name,
                last_name=last_name, username=username, email=email)
        else:
            # Create user account.
            user = User.objects.create_user(
                username, email, password1,
                first_name=first_name, last_name=last_name)
            # notify
            message = "*New Community User:* {} {}".format(
                first_name, last_name)
            utils.send_slack(message)
            return redirect('login')


class CommitGWView(JsonView):
    STATIC_MAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=13&size=640x400"

    def post(self, request, **kwargs):
        data = {}
        for key in ['lat', 'lon', 'rng', 'impact', 'email']:
            data[key] = request.POST.get(key)
        name = request.POST.get('name')
        data['title'] = "{}'s Kickstarter Gateway".format(name)
        if not data['lat'] or not data['lon'] or not name or not data['email']:
            response = {'error': 'Please provide lat, lng, name and email parameters.'}
        else:
            gw = Gateway(**data)
            gw.kickstarter = True
            gw.status = 'PL'
            gw.save()
            response = {'status': 'OK'}
            message = "*Gateway committed* by {}\n".format(name) \
                    + self.STATIC_MAPS_URL.format(**data)
            utils.send_slack(message)
        context = self.get_context_data(**kwargs)
        context['data'] = response
        return self.render_to_response(context)


class ImpactCalculationView(JsonView):

    def get(self, request, **kwargs):
        data = {}
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')
        rng = request.GET.get('rng', 5)
        if not lat or not lng:
            data = {'error': 'Please provide lat and lng parameters.'}
        else:
            try:
                p = population(float(lat), float(lng), float(rng))
                data = {'population': p}
            except Exception as e:
                data = {'error': str(e)}
        context = self.get_context_data(**kwargs)
        context['data'] = data
        return self.render_to_response(context)


def population(lat, lng, rng):
      d = density(lat, lng)
      p = d * (rng ** 2 * math.pi) # circle
      return p


def density(lat, lng):
    headers, data = get_population_data()
    # lat = N-S = 0 (equator) til 90 (N or S)      = y = rows(?) -> some
    # lng = E-W = 0 (GMT) til +180 (E) or -180 (W) = x = cols(?) -> all
    csize = float(headers.get('cellsize'))
    lat_offset = round(float(headers.get('yllcorner')) / csize)
    lng_offset = round(float(headers.get('xllcorner')) / csize)
    lat_count = int(headers.get('nrows'))
    lng_count = int(headers.get('ncols'))
    lat_i = lat_count - (round(lat / csize) - lat_offset)
    lng_i = round(lng / csize) - lng_offset
    print("coords", lat_i, lng_i)
    if lat_i < 0 or lat_i > lat_count or lng_i < 0 or lng_i > lng_count:
        raise ValueError("Location not available on map.")
    # lookup value
    words = data[lat_i].split()
    value = words[lng_i]
    if value == headers.get('NODATA_value'):
        raise ValueError("No data available for given location.")
    return float(value)


def get_population_data():
    fn = os.path.expanduser("/home/ttn/glds00g.asc")
    if not os.path.exists(fn):
        raise Exception("Population data file not found.")
    fp = open(fn, 'r')
    lines = fp.readlines()
  
    headers = {}
    data = []
    for i, line in enumerate(lines):
        words = line.split()
        if len(words) == 2:
            headers[words[0]] = words[1]
        else: # assume all else is data
            data = lines[i:]
            break
    return headers, data
