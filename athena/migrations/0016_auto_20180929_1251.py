# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-29 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0015_auto_20180927_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athenacard',
            name='mugshot',
            field=models.ImageField(blank=True, null=True, upload_to='athena/foodpic'),
        ),
    ]
