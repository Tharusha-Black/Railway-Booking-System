from django.urls import path
from .views import seat_book, reserved_seats, ticket

urlpatterns = [
    path('seat_book/<int:sch_id>', seat_book, name='seat_book'),
    path('reserved_seats/', reserved_seats, name='reserved_seats'),
    path('ticket/', ticket, name='ticket'),
]
