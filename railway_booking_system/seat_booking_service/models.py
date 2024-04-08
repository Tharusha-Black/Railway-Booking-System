from django.db import models
from train_schedule_service.models import TrainSchedule
from user_management.models import RailwayUser

class Seat(models.Model):
    schedule = models.ForeignKey(TrainSchedule, on_delete=models.CASCADE)
    user = models.ForeignKey(RailwayUser, on_delete=models.CASCADE)
    seat_numbers = models.CharField(max_length=50, default='')
