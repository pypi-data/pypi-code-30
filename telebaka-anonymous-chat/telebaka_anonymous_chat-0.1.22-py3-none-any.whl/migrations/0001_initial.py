# Generated by Django 2.0.5 on 2018-07-13 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bots', '0005_auto_20180701_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=64)),
                ('bot', models.ForeignKey(limit_choices_to={'plugin_name': 'telebaka_anonymous_chat'}, on_delete=django.db.models.deletion.CASCADE, to='bots.TelegramBot')),
            ],
        ),
    ]
