# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0016_auto_20150903_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttnuser',
            name='image_thumb_url',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ttnuser',
            name='tagline',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
