# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-17 07:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0018_auto_20181217_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athenacard',
            name='details',
        ),
    ]
