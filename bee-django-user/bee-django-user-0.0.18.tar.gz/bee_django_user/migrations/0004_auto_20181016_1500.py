# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-16 07:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee_django_user', '0003_auto_20180517_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['-created_at'], 'permissions': (('can_manage', '\u53ef\u4ee5\u8bbf\u95ee\u540e\u53f0\u7ba1\u7406'), ('can_change_user_group', '\u53ef\u4ee5\u4fee\u6539\u7528\u6237\u7ec4'), ('reset_user_password', '\u53ef\u4ee5\u91cd\u7f6e\u7528\u6237\u5bc6\u7801'), ('view_all_users', '\u53ef\u4ee5\u67e5\u770b\u6240\u6709\u7528\u6237'), ('view_manage_users', '\u53ef\u4ee5\u67e5\u770b\u7ba1\u7406\u7684\u7528\u6237'), ('view_teach_users', '\u53ef\u4ee5\u67e5\u770b\u6559\u7684\u7528\u6237'))},
        ),
    ]
