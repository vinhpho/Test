# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 20:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0022_auto_20170131_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poke',
            old_name='pokeby',
            new_name='pokedby',
        ),
    ]
