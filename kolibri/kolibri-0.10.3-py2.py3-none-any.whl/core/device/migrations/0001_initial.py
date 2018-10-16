# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-16 23:05
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kolibriauth', '0003_auto_20170621_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevicePermissions',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='devicepermissions', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_superuser', models.BooleanField(default=False)),
                ('can_manage_content', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_provisioned', models.BooleanField(default=False)),
                ('language_id', models.CharField(default='en', max_length=15)),
            ],
        ),
    ]
