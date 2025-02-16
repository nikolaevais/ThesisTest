# Generated by Django 4.2.2 on 2024-11-27 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_doctor_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='job_title',
            field=models.CharField(max_length=100, verbose_name='Должность'),
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Тело письма')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctor', verbose_name='Доктор')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
