# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0022_community_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='description',
            field=models.TextField(blank=True, verbose_name='longer story', null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='mission',
            field=models.TextField(blank=True, verbose_name='short statement', null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='slug',
            field=models.CharField(max_length=200, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='community',
            name='title',
            field=models.CharField(max_length=200, verbose_name='area name'),
        ),
    ]
