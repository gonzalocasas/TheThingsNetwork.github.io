#from django.forms import ModelForm
from django.contrib.gis import forms

from .models import Community, Post


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['mission', 'description', 'contact',
                  'coords', 'scale',
                  'meetup_url', 'twitter_handle',
                  'image_url', 'image_thumb_url',
                 ]
        widgets = {
            # https://docs.djangoproject.com/en/1.8/ref/forms/widgets/
            'coords': forms.OSMWidget(attrs={'map_width': 900}), # alternative widget
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'description']

