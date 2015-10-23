from django.db import models
from django.contrib.auth.models import User


class TTNUser(models.Model):
    # See: https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#extending-the-existing-user-model
    user = models.OneToOneField(User)
    tagline = models.CharField(max_length=200, blank=True, null=True)
    #image_thumb = models.ImageField('Picture', blank=True, null=True)
    image_thumb_url = models.CharField(max_length=250, blank=True, null=True)
    twitter_handle = models.CharField(max_length=250, blank=True, null=True)


class Gateway(models.Model):
    STATUS_CHOICES = [
        ('PL', 'Planned'),
        ('AC', 'Active'),
        ('MA', 'Maintenance'),
        ('DE', 'Deprecated')
    ]
    # TODO: use GeoDjango fields (for fast geo queries)
    # https://docs.djangoproject.com/en/dev/ref/contrib/gis/
    lat = models.FloatField('latitude', blank=True, null=True)
    lon = models.FloatField('longitude', blank=True, null=True)
    rng = models.FloatField('Range (m)', default=5000)
    title = models.CharField(max_length=200)
    kickstarter = models.BooleanField(default=False)
    email = models.CharField(max_length=200, blank=True, null=True)
    impact = models.IntegerField('Impact (people)', blank=True, null=True)
    owner_human = models.ForeignKey(User, null=True, blank=True)
    owner_company = models.ForeignKey('Company', null=True, blank=True)
    message_count = models.IntegerField(default=0, null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES,
                              default='AC')
    gateway_eui = models.CharField(max_length=32, null=True, blank=True)
    auto_update = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Community(models.Model):
    # TODO: use area type
    lat = models.FloatField('latitude', blank=True, null=True)
    lon = models.FloatField('longitude', blank=True, null=True)
    scale = models.FloatField('Scale (zoom)', default=13)
    published = models.BooleanField(default=True)
    slug = models.CharField(max_length=200)
    slug.help_text = 'url'
    title = models.CharField(max_length=200)
    title.help_text = 'Area name'
    mission = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description.help_text = 'Get them excited'
    contact = models.TextField(blank=True, null=True)
    #image = models.ImageField('City image', blank=True, null=True)
    image_url = models.CharField(max_length=250)
    image_thumb_url = models.CharField(max_length=250)
    meetup_url = models.CharField(max_length=250, blank=True, null=True)
    twitter_handle = models.CharField(max_length=250, blank=True, null=True)
    leaders = models.ManyToManyField(User, related_name="Leaders")
    members = models.ManyToManyField(User, related_name="Members")
    companies = models.ManyToManyField('Company', related_name="Companies",
                                       blank=True)
    gateways = models.ManyToManyField(Gateway, related_name="Gateways",
                                      blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} <{}, {}>".format(self.title, self.lat, self.lon)


class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    community = models.ForeignKey(Community, null=True, blank=True)
    slug = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    #image = models.ImageField('City image', blank=True, null=True)
    image_url = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        c = self.community.title if self.community else '*'
        return "[{}] {}".format(c, self.title)


class Media(models.Model):
    """Media attention for specific community"""
    author = models.ForeignKey(User, null=True, blank=True)
    community = models.ForeignKey(Community, null=True, blank=True)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        c = self.community.title if self.community else '*'
        return "[{}] {}".format(c, self.title)


class Resource(models.Model):
    """External resource for community (github, meetup group, ..)"""
    author = models.ForeignKey(User, null=True, blank=True)
    community = models.ForeignKey(Community, null=True, blank=True)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        c = self.community.title if self.community else '*'
        return "[{}] {}".format(c, self.title)


class Company(models.Model):
    """Companies wanting exposure"""
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=250)
    #image_logo = models.ImageField('Picture', blank=True, null=True)
    image_logo_url = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class InitiatorSubmission(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    url = models.CharField(max_length=250)
    skills = models.TextField(blank=True, null=True)
    area = models.CharField(max_length=200)
    contributors = models.TextField(blank=True, null=True)
    plan = models.TextField(blank=True, null=True)
    helping = models.TextField(blank=True, null=True)
    internal_comments = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "[{}] {} <{}>".format(self.area, self.name, self.email)

