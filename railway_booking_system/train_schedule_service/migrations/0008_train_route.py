# Generated by Django 5.0.3 on 2024-04-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train_schedule_service', '0007_rename_route_trainschedule_destination_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='route',
            field=models.CharField(default='', max_length=50),
        ),
    ]