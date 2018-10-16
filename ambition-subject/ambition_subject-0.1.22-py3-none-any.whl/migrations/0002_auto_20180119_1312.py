# Generated by Django 2.0.1 on 2018-01-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='rankin_score',
            field=models.CharField(choices=[('0', '0 - No symptoms at all'), ('1', '1 - No significant disability despite symptoms; able to carry out all usual duties and activities'), ('2', '2 - Slight disability; unable to carry out all previous activities, but able to look after own affairs without assistance'), ('3', '3 - Moderate disability; requiring some help, but able to walk without assistance'), ('4', '4 - Moderately severe disability; unable to walk without assistance and unable to attend to own bodily needs without assistance'), ('5', '5 - Severe disability; bedridden, incontinent and requiring constant nursing care and attention'), ('6', '6 - Dead'), ('not_done', 'Not done')], max_length=10, null=True, verbose_name='Modified Rankin score'),
        ),
        migrations.AlterField(
            model_name='historicalfollowup',
            name='rankin_score',
            field=models.CharField(choices=[('0', '0 - No symptoms at all'), ('1', '1 - No significant disability despite symptoms; able to carry out all usual duties and activities'), ('2', '2 - Slight disability; unable to carry out all previous activities, but able to look after own affairs without assistance'), ('3', '3 - Moderate disability; requiring some help, but able to walk without assistance'), ('4', '4 - Moderately severe disability; unable to walk without assistance and unable to attend to own bodily needs without assistance'), ('5', '5 - Severe disability; bedridden, incontinent and requiring constant nursing care and attention'), ('6', '6 - Dead'), ('not_done', 'Not done')], max_length=10, null=True, verbose_name='Modified Rankin score'),
        ),
        migrations.AlterField(
            model_name='historicalweek16',
            name='rankin_score',
            field=models.CharField(choices=[('0', '0 - No symptoms at all'), ('1', '1 - No significant disability despite symptoms; able to carry out all usual duties and activities'), ('2', '2 - Slight disability; unable to carry out all previous activities, but able to look after own affairs without assistance'), ('3', '3 - Moderate disability; requiring some help, but able to walk without assistance'), ('4', '4 - Moderately severe disability; unable to walk without assistance and unable to attend to own bodily needs without assistance'), ('5', '5 - Severe disability; bedridden, incontinent and requiring constant nursing care and attention'), ('6', '6 - Dead'), ('not_done', 'Not done')], max_length=10, verbose_name='Modified Rankin score'),
        ),
        migrations.AlterField(
            model_name='week16',
            name='rankin_score',
            field=models.CharField(choices=[('0', '0 - No symptoms at all'), ('1', '1 - No significant disability despite symptoms; able to carry out all usual duties and activities'), ('2', '2 - Slight disability; unable to carry out all previous activities, but able to look after own affairs without assistance'), ('3', '3 - Moderate disability; requiring some help, but able to walk without assistance'), ('4', '4 - Moderately severe disability; unable to walk without assistance and unable to attend to own bodily needs without assistance'), ('5', '5 - Severe disability; bedridden, incontinent and requiring constant nursing care and attention'), ('6', '6 - Dead'), ('not_done', 'Not done')], max_length=10, verbose_name='Modified Rankin score'),
        ),
    ]
