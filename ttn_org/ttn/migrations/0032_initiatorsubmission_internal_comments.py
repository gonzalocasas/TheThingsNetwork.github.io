# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0031_gateway_impact'),
    ]

    operations = [
        migrations.AddField(
            model_name='initiatorsubmission',
            name='internal_comments',
            field=models.TextField(null=True, blank=True),
        ),
    ]
