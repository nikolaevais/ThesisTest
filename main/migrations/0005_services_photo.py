# Generated by Django 4.2.2 on 2024-11-28 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_doctor_job_title_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='main/services/photo/', verbose_name='Фото'),
        ),
    ]