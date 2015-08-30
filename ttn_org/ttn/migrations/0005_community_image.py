# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0004_community_gateways'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='image',
            field=models.ImageField(verbose_name='City image', blank=True, upload_to='', null=True),
        ),
    ]
