# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-12-06 20:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kolibriauth', '0005_auto_20170818_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='kind',
            field=models.CharField(choices=[('facility', 'Facility'), ('classroom', 'Classroom'), ('learnergroup', 'Learner group')], max_length=20),
        ),
        migrations.AlterField(
            model_name='facilitydataset',
            name='preset',
            field=models.CharField(choices=[('informal', 'Informal and personal use'), ('formal', 'Admin-managed'), ('nonformal', 'Self-managed')], default='nonformal', max_length=50),
        ),
        migrations.AlterField(
            model_name='facilityuser',
            name='username',
            field=models.CharField(help_text='Required. 30 characters or fewer. Letters and digits only', max_length=30, validators=[django.core.validators.RegexValidator('^\\w+$', 'Enter a valid username. This value can contain only letters, numbers, and underscores.')], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='role',
            name='kind',
            field=models.CharField(choices=[('admin', 'Admin'), ('coach', 'Coach')], max_length=20),
        ),
    ]
