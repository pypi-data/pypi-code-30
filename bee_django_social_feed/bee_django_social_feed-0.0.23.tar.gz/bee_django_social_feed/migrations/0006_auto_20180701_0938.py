# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-01 01:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee_django_social_feed', '0005_albumphoto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albumphoto',
            options={'ordering': ['-created_at']},
        ),
    ]
