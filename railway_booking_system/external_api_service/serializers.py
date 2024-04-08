# serializers.py

from rest_framework import serializers
from train_schedule_service.models import Train, TrainSchedule

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'

class TrainScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainSchedule
        fields = '__all__'
