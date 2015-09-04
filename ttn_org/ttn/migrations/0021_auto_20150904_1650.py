# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0020_auto_20150904_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='mission',
            field=models.TextField(null=True, blank=True),
        ),
    ]
