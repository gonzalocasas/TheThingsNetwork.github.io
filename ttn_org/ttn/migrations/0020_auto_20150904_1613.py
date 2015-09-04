# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0019_gateway_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='mission',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='gateway',
            name='message_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
