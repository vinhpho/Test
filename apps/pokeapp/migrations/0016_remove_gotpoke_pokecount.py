# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 05:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0015_auto_20170130_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gotpoke',
            name='pokecount',
        ),
    ]
