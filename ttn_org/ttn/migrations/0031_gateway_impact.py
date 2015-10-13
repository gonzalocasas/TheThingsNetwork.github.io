# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0030_auto_20151013_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='gateway',
            name='impact',
            field=models.IntegerField(blank=True, verbose_name='Impact (people)', null=True),
        ),
    ]
