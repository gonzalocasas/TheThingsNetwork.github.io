# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0035_auto_20151026_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='initiatorsubmission',
            name='community',
            field=models.ForeignKey(to='ttn.Community', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='image_url',
            field=models.CharField(blank=True, null=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='community',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='community',
            name='slug',
            field=models.CharField(help_text='url', unique=True, max_length=200),
        ),
    ]
