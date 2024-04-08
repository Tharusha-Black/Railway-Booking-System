from django.urls import path,include
from . import views

urlpatterns = [
    path('add_train/', views.add_train, name='add_train'),
    path('schedule_train/', views.schedule_train, name='schedule_train'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('edit_train/<int:train_id>/', views.edit_train, name='edit_train'),
    path('delete_train/<int:train_id>/', views.delete_train, name='delete_train'),
    path('edit_schedule/<int:schedule_id>/', views.edit_schedule, name='edit_schedule'),
    path('delete_schedule/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),

]
