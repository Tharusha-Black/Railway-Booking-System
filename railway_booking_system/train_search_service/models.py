from django.db import models

class Train(models.Model):
    name = models.CharField(max_length=100)
    start_station = models.CharField(max_length=100)
    destination_station = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    # Add more fields as needed
