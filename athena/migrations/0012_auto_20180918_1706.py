# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-18 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0011_auto_20180918_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athenacard',
            name='category',
            field=models.CharField(choices=[('TD', 'Tandoori'), ('CB', 'Cold Beverage'), ('IT', 'Italian'), ('HT', 'Healthy'), ('DS', 'Dessert'), ('SP', 'Specialties')], max_length=2),
        ),
    ]