# Generated by Django 4.0.4 on 2022-05-21 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyStudyPlanAPI', '0012_assessment_alter_tasks_taskduedate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assessment',
            new_name='Assessments',
        ),
    ]
