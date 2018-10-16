# Generated by Django 2.1 on 2018-10-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_locator', '0014_auto_20181009_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubjectlocator',
            name='action_identifier',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalsubjectlocator',
            name='parent_action_identifier',
            field=models.CharField(help_text='action identifier that links to parent reference model instance.', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='historicalsubjectlocator',
            name='related_action_identifier',
            field=models.CharField(help_text='action identifier that links to related reference model instance.', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='subjectlocator',
            name='action_identifier',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='subjectlocator',
            name='parent_action_identifier',
            field=models.CharField(help_text='action identifier that links to parent reference model instance.', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='subjectlocator',
            name='related_action_identifier',
            field=models.CharField(help_text='action identifier that links to related reference model instance.', max_length=30, null=True),
        ),
    ]
