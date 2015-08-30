# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0002_community_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ttnuser',
            name='user',
        ),
        migrations.AlterField(
            model_name='community',
            name='leaders',
            field=models.ManyToManyField(related_name='Leaders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(related_name='Members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gateway',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='TTNUser',
        ),
    ]
