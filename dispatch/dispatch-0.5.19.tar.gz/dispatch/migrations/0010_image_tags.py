# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-17 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0008_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(to='dispatch.Tag'),
        ),
    ]
