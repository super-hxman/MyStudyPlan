# Generated by Django 4.0.4 on 2022-05-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyStudyPlanAPI', '0007_modules_modulegrade'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='TaskDueDate',
            field=models.DateField(default='2022-05-17'),
        ),
    ]
