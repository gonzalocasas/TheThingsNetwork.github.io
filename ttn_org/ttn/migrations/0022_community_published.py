# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0021_auto_20150904_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
