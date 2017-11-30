# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-29 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20171129_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='credentials',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='credentials',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
