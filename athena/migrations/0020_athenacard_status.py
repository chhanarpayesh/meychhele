# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-18 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0019_remove_athenacard_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='athenacard',
            name='status',
            field=models.CharField(choices=[('f', 'Carnal Knowledge'), ('m', 'Tie the knot')], max_length=20, null=True),
        ),
    ]
