"""
URL configuration for railway_booking_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('train_search_service/', include('train_search_service.urls')),
    path('seat_booking_service/', include('seat_booking_service.urls')),
    path('train_schedule_service/', include('train_schedule_service.urls')),
    path('external_api_service/', include('external_api_service.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='user_management/login.html'), name='login'),
    path('', include('user_management.urls'))

]
