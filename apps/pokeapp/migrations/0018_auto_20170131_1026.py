# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0017_auto_20170131_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='pokeothertotal',
            field=models.IntegerField(default=0),
        ),
    ]
