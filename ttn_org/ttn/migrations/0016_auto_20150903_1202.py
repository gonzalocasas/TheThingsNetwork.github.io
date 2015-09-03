# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0015_auto_20150903_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='companies',
            field=models.ManyToManyField(to='ttn.Company', blank=True, related_name='Companies'),
        ),
        migrations.AlterField(
            model_name='community',
            name='gateways',
            field=models.ManyToManyField(to='ttn.Gateway', blank=True, related_name='Gateways'),
        ),
    ]
