from django.urls import path
from .views import SearchTrainsView

urlpatterns = [
    path('search_trains/', SearchTrainsView.as_view(), name='search_trains'),
]
