# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-16 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='athenacard',
            name='mugshot',
            field=models.ImageField(max_length=120, null=True, upload_to='photos/miha'),
        ),
    ]
