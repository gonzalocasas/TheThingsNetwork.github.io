# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0037_keyvalue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
    ]
