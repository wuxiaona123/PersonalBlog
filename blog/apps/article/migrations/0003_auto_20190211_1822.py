# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-11 18:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190211_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tagmodels',
            old_name='parentid',
            new_name='parent',
        ),
    ]
