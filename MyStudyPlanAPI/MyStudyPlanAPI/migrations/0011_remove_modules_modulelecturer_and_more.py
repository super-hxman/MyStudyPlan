# Generated by Django 4.0.4 on 2022-05-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyStudyPlanAPI', '0010_modules_modulecolor_modules_moduletype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modules',
            name='ModuleLecturer',
        ),
        migrations.AlterField(
            model_name='tasks',
            name='TaskDueDate',
            field=models.DateField(default='2022-05-19'),
        ),
    ]
