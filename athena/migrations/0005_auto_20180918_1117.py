# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-18 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0004_auto_20180816_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athenacard',
            name='mugshot',
            field=models.ImageField(blank=True, max_length=120, null=True, upload_to='miha'),
        ),
    ]
