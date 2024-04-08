from django.urls import path
from .views import search_trains

urlpatterns = [
    path('search_trains/', search_trains, name='search_trains'),
]
