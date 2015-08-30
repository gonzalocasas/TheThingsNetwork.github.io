# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0005_community_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='image',
        ),
        migrations.AddField(
            model_name='community',
            name='image_url',
            field=models.CharField(max_length=250, default=''),
            preserve_default=False,
        ),
    ]
