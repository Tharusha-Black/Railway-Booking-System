from django.db import models
from datetime import date 

class Train(models.Model):
    train_name = models.CharField(max_length=100, default='')
    route = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.train_name

class TrainSchedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    schedule_date = models.DateField(default=date.today)
    departure_time = models.CharField(max_length=100, default='')
    start_location = models.CharField(max_length=50, default='')
    destination = models.CharField(max_length=50, default='')

    def __str__(self):
        return f"{self.train.train_name} - {self.schedule_date}"
