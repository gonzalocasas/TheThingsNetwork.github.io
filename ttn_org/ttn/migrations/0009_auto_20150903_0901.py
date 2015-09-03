# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0008_community_image_thumb_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='contact',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='gateways',
            field=models.ManyToManyField(null=True, blank=True, related_name='Gateways', to='ttn.Gateway'),
        ),
    ]
