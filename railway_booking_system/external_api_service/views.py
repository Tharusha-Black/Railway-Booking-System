from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from train_schedule_service.models import Train, TrainSchedule
from .serializers import TrainSerializer, TrainScheduleSerializer

class TrainListView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # Retrieve all trains from the database
        trains = Train.objects.all()

        # Serialize the trains data
        serializer = TrainSerializer(trains, many=True)

        # Return the serialized data as a JSON response
        return Response(serializer.data)

class ScheduleListView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # Retrieve all train schedules from the database
        schedules = TrainSchedule.objects.all()

        # Serialize the schedules data
        serializer = TrainScheduleSerializer(schedules, many=True)

        # Return the serialized data as a JSON response
        return Response(serializer.data)
