# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='time',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
