# Generated by Django 5.1.1 on 2024-09-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_attendancerecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='attendance_status',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Doubt', 'Doubt')], max_length=20),
        ),
    ]
