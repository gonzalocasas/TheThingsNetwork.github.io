# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0007_media_post_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='image_thumb_url',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
