# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 03:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0011_auto_20170130_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whopoke',
            old_name='name',
            new_name='gotpoke',
        ),
        migrations.RenameField(
            model_name='whopoke',
            old_name='pokewho',
            new_name='whopoke',
        ),
    ]
