# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-04-24 19:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0031_auto_20190425_0101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athenavideofile',
            old_name='person',
            new_name='athena',
        ),
    ]