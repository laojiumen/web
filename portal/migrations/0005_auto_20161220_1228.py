# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20161220_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biggod',
            name='english_name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='biggod',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
    ]