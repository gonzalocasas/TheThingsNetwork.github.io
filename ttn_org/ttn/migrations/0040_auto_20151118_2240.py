# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0039_gateway_coords'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gateway',
            old_name='lat',
            new_name='lat_old',
        ),
        migrations.RenameField(
            model_name='gateway',
            old_name='lon',
            new_name='lon_old',
        ),
    ]
