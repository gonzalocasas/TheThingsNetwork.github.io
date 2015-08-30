# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='slug',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]
