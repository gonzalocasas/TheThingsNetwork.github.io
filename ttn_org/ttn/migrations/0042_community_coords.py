# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0041_auto_20151119_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='coords',
            field=django.contrib.gis.db.models.fields.PointField(null=True, blank=True, verbose_name='coordinates', srid=4326),
        ),
    ]
