# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-17 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(default='my job default', max_length=120),
        ),
    ]
