# Generated by Django 2.0.5 on 2018-08-24 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telebaka_anonymous_chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='media_sent',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
