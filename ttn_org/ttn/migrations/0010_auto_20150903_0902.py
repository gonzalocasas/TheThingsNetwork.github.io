# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0009_auto_20150903_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='contact',
            field=models.TextField(null=True, blank=True),
        ),
    ]
