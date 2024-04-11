from django.urls import path
from .views import SeatBookView, SeatReservationView

urlpatterns = [
    path('seat_book/<int:sch_id>/', SeatBookView.as_view(), name='seat_book'),
    path('reserved_seats/', SeatReservationView.as_view(), name='reserved_seats'),
]
