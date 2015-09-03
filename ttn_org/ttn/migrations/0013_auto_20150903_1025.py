# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0012_auto_20150903_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttnuser',
            name='tagline',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='community',
            name='scale',
            field=models.FloatField(default=13, verbose_name='Scale (m)'),
        ),
    ]
