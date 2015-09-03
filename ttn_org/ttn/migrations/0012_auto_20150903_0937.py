# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0011_ttnuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ttnuser',
            name='image',
        ),
        migrations.AddField(
            model_name='ttnuser',
            name='image_thumb_url',
            field=models.CharField(max_length=250, default=''),
            preserve_default=False,
        ),
    ]
