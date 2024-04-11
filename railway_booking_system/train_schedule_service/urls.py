from django.urls import path,include
from .views import DashboardView, EditTrainView, DeleteTrainView, AddTrainView, ScheduleTrainView, EditScheduleView, DeleteScheduleView

urlpatterns = [
    path('add_train/', AddTrainView.as_view(), name='add_train'),
    path('schedule_train/', ScheduleTrainView.as_view(), name='schedule_train'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('edit_train/<int:train_id>/', EditTrainView.as_view(), name='edit_train'),
    path('delete_train/<int:train_id>/', DeleteTrainView.as_view(), name='delete_train'),
    path('edit_schedule/<int:schedule_id>/', EditScheduleView.as_view(), name='edit_schedule'),
    path('delete_schedule/<int:schedule_id>/', DeleteScheduleView.as_view(), name='delete_schedule'),
]
