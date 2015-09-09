# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0023_auto_20150909_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='description',
            field=models.TextField(help_text='Get them excited', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='mission',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='slug',
            field=models.CharField(help_text='url', max_length=200),
        ),
        migrations.AlterField(
            model_name='community',
            name='title',
            field=models.CharField(help_text='Area name', max_length=200),
        ),
    ]
