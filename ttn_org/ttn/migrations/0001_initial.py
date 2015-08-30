# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('lat', models.FloatField(null=True, verbose_name='latitude', blank=True)),
                ('lon', models.FloatField(null=True, verbose_name='longitude', blank=True)),
                ('scale', models.FloatField(default=25000, verbose_name='Scale (m)')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('lat', models.FloatField(null=True, verbose_name='latitude', blank=True)),
                ('lon', models.FloatField(null=True, verbose_name='longitude', blank=True)),
                ('rng', models.FloatField(default=5000, verbose_name='Range (m)')),
                ('title', models.CharField(max_length=200)),
                ('message_count', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TTNUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Picture', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gateway',
            name='owner',
            field=models.ForeignKey(null=True, to='ttn.TTNUser', blank=True),
        ),
        migrations.AddField(
            model_name='community',
            name='leaders',
            field=models.ManyToManyField(related_name='Leaders', to='ttn.TTNUser'),
        ),
        migrations.AddField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(related_name='Members', to='ttn.TTNUser'),
        ),
    ]
