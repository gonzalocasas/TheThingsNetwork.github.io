# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0017_auto_20150904_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gateway',
            old_name='owner',
            new_name='owner_human',
        ),
        migrations.AddField(
            model_name='gateway',
            name='owner_company',
            field=models.ForeignKey(blank=True, null=True, to='ttn.Company'),
        ),
    ]
