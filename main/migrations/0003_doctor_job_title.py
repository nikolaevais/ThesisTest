# Generated by Django 4.2.2 on 2024-11-27 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_doctor_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='job_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность'),
        ),
    ]
