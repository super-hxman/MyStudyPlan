# Generated by Django 4.0.4 on 2022-04-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyStudyPlanAPI', '0002_schedules_alter_modules_modulecode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('ChapterId', models.AutoField(primary_key=True, serialize=False)),
                ('ChapterName', models.CharField(max_length=100)),
                ('ChapterStatus', models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Ready', 'Ready'), ('Completed', 'Completed')], default='New', max_length=20)),
            ],
        ),
    ]
