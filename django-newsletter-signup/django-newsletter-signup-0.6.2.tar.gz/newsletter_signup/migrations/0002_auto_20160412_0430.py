# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 04:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersignup',
            name='first_name',
            field=models.CharField(blank=True, max_length=512, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='newslettersignup',
            name='last_name',
            field=models.CharField(blank=True, max_length=512, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='newslettersignup',
            name='referer',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='newslettersignup',
            name='source',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='newslettersignup',
            name='email',
            field=models.EmailField(max_length=1024, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='newslettersignup',
            name='signup_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='signup date'),
        ),
        migrations.AlterField(
            model_name='newslettersignup',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
