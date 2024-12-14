# Generated by Django 5.1.4 on 2024-12-14 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school1', '0002_student_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='student_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.TextField(blank=True),
        ),
    ]
