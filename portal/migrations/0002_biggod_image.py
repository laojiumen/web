# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biggod',
            name='image',
            field=models.ImageField(default='', upload_to=b''),
        ),
    ]
