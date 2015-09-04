# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0018_auto_20150904_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='gateway',
            name='status',
            field=models.CharField(choices=[('PL', 'Planned'), ('AC', 'Active'), ('MA', 'Maintenance'), ('DE', 'Deprecated')], default='AC', max_length=2),
        ),
    ]
