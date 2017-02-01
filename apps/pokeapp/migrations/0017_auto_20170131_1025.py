# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 16:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0016_remove_gotpoke_pokecount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gotpoke',
            name='pokeby',
        ),
        migrations.AddField(
            model_name='gotpoke',
            name='pokeby',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pokeapp.User'),
            preserve_default=False,
        ),
    ]
