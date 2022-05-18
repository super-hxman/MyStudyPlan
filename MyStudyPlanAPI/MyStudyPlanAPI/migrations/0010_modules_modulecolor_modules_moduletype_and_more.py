# Generated by Django 4.0.4 on 2022-05-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyStudyPlanAPI', '0009_delete_schedules'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='ModuleColor',
            field=models.CharField(default='White', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modules',
            name='ModuleType',
            field=models.CharField(choices=[('Core', 'Core'), ('Workshop', 'Workshop')], default='Core', max_length=10),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='TaskDueDate',
            field=models.DateField(default='2022-05-18'),
        ),
    ]