# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-05 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='opinion',
        ),
        migrations.AddField(
            model_name='comment',
            name='axe',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='image', to='images.Image'),
            preserve_default=False,
        ),
    ]
