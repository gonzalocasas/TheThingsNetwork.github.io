# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0042_community_coords'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='gateways',
            new_name='gateways_old',
        ),
    ]
