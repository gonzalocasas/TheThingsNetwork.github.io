# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0038_auto_20151106_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='gateway',
            name='coords',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, verbose_name='coordinates', null=True, srid=4326),
        ),
    ]
