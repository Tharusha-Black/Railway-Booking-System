# Generated by Django 5.0.3 on 2024-04-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train_schedule_service', '0006_remove_train_train_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainschedule',
            old_name='route',
            new_name='destination',
        ),
        migrations.RemoveField(
            model_name='train',
            name='route_1',
        ),
        migrations.RemoveField(
            model_name='train',
            name='route_2',
        ),
        migrations.AddField(
            model_name='trainschedule',
            name='start_location',
            field=models.CharField(default='', max_length=50),
        ),
    ]
