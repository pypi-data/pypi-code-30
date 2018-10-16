# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 01:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=64, verbose_name='Email')),
                ('signup_date', models.DateTimeField(auto_now_add=True, verbose_name='Signup date')),
                ('verification_token', models.UUIDField(blank=True, null=True, verbose_name='Verification token')),
                ('verification_date', models.DateTimeField(blank=True, null=True, verbose_name='Verification date')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
