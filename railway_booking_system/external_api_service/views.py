from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from train_schedule_service.models import Train, TrainSchedule
from .serializers import TrainSerializer, TrainScheduleSerializer

class TrainListView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        trains = Train.objects.all()
        serializer = TrainSerializer(trains, many=True)
        return Response(serializer.data)

class ScheduleListView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        schedules = TrainSchedule.objects.all()
        serializer = TrainScheduleSerializer(schedules, many=True)
        return Response(serializer.data)
