# Generated by Django 5.0.3 on 2024-04-07 03:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train_schedule_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(default='', max_length=100)),
                ('train_tag', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='trainschedule',
            name='destination',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='trainschedule',
            name='schedule_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='trainschedule',
            name='start_location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='departure_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train_schedule_service.train'),
        ),
    ]