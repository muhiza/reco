# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_wine_wine_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
