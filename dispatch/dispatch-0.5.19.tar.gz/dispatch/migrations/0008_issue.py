# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-28 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0007_preview_id_remove_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to=b'issues/%Y/%m')),
                ('img', models.ImageField(upload_to=b'images/%Y/%m')),
                ('issue', models.PositiveIntegerField(null=True)),
                ('volume', models.PositiveIntegerField(null=True)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
