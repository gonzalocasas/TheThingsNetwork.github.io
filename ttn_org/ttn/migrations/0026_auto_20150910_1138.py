# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0025_post_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='gateway',
            name='auto_update',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='gateway',
            name='gateway_eui',
            field=models.CharField(null=True, max_length=32, blank=True),
        ),
    ]
