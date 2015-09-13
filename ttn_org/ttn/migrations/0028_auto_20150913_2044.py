# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0027_initiatorsubmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='scale',
            field=models.FloatField(default=13, verbose_name='Scale (zoom)'),
        ),
    ]
