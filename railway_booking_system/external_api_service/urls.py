# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/trains/', views.TrainListView.as_view(), name='train-list'),
    path('api/schedules/', views.ScheduleListView.as_view(), name='schedule-list'),
    # Add more API endpoints as needed
]
