# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-19 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0029_auto_20181219_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athenacard',
            old_name='imcomplete',
            new_name='incomplete',
        ),
    ]
