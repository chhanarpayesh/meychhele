# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-29 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0016_auto_20180929_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athenacard',
            name='category',
            field=models.CharField(choices=[('tandoori', 'Tandoori'), ('cold_beverage', 'Cold Beverage'), ('italian', 'Italian'), ('healthy', 'Healthy'), ('dessert', 'Dessert'), ('specialties', 'Specialties')], max_length=20),
        ),
    ]