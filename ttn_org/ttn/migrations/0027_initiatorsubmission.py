# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttn', '0026_auto_20150910_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitiatorSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=250)),
                ('skills', models.TextField(blank=True, null=True)),
                ('area', models.CharField(max_length=200)),
                ('contributors', models.TextField(blank=True, null=True)),
                ('plan', models.TextField(blank=True, null=True)),
                ('helping', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
