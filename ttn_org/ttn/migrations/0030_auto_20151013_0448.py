# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0029_auto_20151006_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='gateway',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='gateway',
            name='kickstarter',
            field=models.BooleanField(default=False),
        ),
    ]
