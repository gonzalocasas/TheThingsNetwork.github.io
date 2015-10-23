# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0032_initiatorsubmission_internal_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='meetup_url',
            field=models.CharField(blank=True, null=True, max_length=250),
        ),
        migrations.AddField(
            model_name='community',
            name='twitter_handle',
            field=models.CharField(blank=True, null=True, max_length=250),
        ),
        migrations.AddField(
            model_name='ttnuser',
            name='twitter_handle',
            field=models.CharField(blank=True, null=True, max_length=250),
        ),
    ]
