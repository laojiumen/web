# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_remove_biggod_github'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biggod',
            old_name='description',
            new_name='tags',
        ),
    ]