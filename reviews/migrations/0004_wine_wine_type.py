# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20170518_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='wine_type',
            field=models.IntegerField(choices=[(1, 'red'), (2, 'green'), (3, 'blue')], null=True),
        ),
    ]
