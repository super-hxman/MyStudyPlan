# Generated by Django 4.0.4 on 2022-05-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyStudyPlanAPI', '0005_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='ModuleStatus',
            field=models.CharField(choices=[('Active', 'Active'), ('Completed', 'Completed')], default='Active', max_length=20),
        ),
    ]
