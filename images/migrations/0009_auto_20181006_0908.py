# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-06 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0008_auto_20181006_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
