# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-18 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0023_auto_20181218_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athenacard',
            name='dob',
            field=models.DateField(blank=True, default='01/01/89', null=True),
        ),
    ]
