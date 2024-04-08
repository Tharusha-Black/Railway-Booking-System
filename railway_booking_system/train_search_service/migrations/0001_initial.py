# Generated by Django 5.0.3 on 2024-04-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_station', models.CharField(max_length=100)),
                ('destination_station', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField()),
            ],
        ),
    ]