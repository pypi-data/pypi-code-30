# Generated by Django 2.1 on 2018-08-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_registration', '0012_auto_20180116_1528'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registeredsubject',
            unique_together={
                ('first_name', 'dob', 'initials', 'additional_key')},
        ),
        migrations.AddIndex(
            model_name='registeredsubject',
            index=models.Index(fields=['first_name', 'dob', 'initials',
                                       'additional_key'], name='edc_registr_first_n_a70796_idx'),
        ),
        migrations.AddIndex(
            model_name='registeredsubject',
            index=models.Index(fields=['identity', 'subject_identifier',
                                       'screening_identifier'], name='edc_registr_identit_eb36e0_idx'),
        ),
    ]
