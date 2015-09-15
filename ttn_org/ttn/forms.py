from django.forms import ModelForm

from .models import Community, Post


class SettingsForm(ModelForm):
    class Meta:
        model = Community
        fields = ['mission', 'description', 'contact',
                  'lat', 'lon', 'scale',
                  'image_url', 'image_thumb_url',
                 ]
        widgets = {
            # https://docs.djangoproject.com/en/1.8/ref/forms/widgets/
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'description']

