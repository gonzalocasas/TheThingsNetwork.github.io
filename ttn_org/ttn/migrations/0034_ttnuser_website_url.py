# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0033_auto_20151023_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttnuser',
            name='website_url',
            field=models.CharField(blank=True, null=True, max_length=250),
        ),
    ]
