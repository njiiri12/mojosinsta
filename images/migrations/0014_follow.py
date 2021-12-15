# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 08:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0013_auto_20181007_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c_user', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='follow', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]