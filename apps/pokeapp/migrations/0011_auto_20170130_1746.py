# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 23:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0010_poke_pokecount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='poke',
            new_name='whopoke',
        ),
        migrations.RenameField(
            model_name='whopoke',
            old_name='pokes',
            new_name='pokewho',
        ),
    ]
