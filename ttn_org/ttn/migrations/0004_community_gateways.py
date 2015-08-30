# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0003_auto_20150830_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='gateways',
            field=models.ManyToManyField(to='ttn.Gateway', related_name='Gateways'),
        ),
    ]
