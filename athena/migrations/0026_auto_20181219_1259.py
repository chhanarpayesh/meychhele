# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-19 07:29
from __future__ import unicode_literals

import athena.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('athena', '0025_auto_20181219_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='AthenaRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(blank=True, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-rank',),
            },
        ),
        migrations.AlterField(
            model_name='athenacard',
            name='mugshot',
            field=models.ImageField(blank=True, null=True, upload_to=athena.models.AthenaCard.update_image_file),
        ),
        migrations.AddField(
            model_name='athenarank',
            name='athena',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athena.AthenaCard'),
        ),
        migrations.AddField(
            model_name='athenarank',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
