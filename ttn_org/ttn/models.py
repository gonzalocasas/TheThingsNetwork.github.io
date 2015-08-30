from django.db import models
from django.contrib.auth.models import User


#class TTNUser(models.Model):
#    # See: https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#extending-the-existing-user-model
#    user = models.OneToOneField(User)
#    image = models.ImageField('Picture', blank=True, null=True)


class Gateway(models.Model):
    # TODO: use GeoDjango fields (for fast geo queries)
    # https://docs.djangoproject.com/en/dev/ref/contrib/gis/
    lat = models.FloatField('latitude', blank=True, null=True)
    lon = models.FloatField('longitude', blank=True, null=True)
    rng = models.FloatField('Range (m)', default=5000)
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, null=True, blank=True)
    message_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Community(models.Model):
    # TODO: use area type
    lat = models.FloatField('latitude', blank=True, null=True)
    lon = models.FloatField('longitude', blank=True, null=True)
    scale = models.FloatField('Scale (m)', default=25000)
    slug = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    leaders = models.ManyToManyField(User, related_name="Leaders")
    members = models.ManyToManyField(User, related_name="Members")

    def __str__(self):
        return "{} <{}, {}>".format(self.title, self.lat, self.lon)

