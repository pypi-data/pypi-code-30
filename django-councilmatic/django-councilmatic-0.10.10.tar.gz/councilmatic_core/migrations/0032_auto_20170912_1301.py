# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-12 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('councilmatic_core', '0031_eventdocument_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='bill',
            name='subject',
        ),
        migrations.AlterField(
            model_name='eventdocument',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='councilmatic_core.Bill'),
        ),
    ]
