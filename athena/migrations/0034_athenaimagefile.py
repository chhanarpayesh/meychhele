# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-04-24 20:31
from __future__ import unicode_literals

import athena.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0033_auto_20190425_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='AthenaImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to=athena.models.AthenaImageFile.update_img_file)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('athena', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athena.AthenaCard')),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
    ]