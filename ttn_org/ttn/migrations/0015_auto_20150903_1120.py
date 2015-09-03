# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0014_auto_20150903_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='companies',
            field=models.ManyToManyField(null=True, related_name='Companies', to='ttn.Company', blank=True),
        ),
    ]
