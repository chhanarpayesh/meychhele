# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-16 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0002_athenacard_mugshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='athenacard',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]