# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-09 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bee_django_social_feed', '0011_auto_20180709_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedimage',
            name='medium_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='feedimage',
            name='thumbnail_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
