# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 22:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0024_auto_20170131_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='PokeHistory',
            new_name='time',
        ),
    ]