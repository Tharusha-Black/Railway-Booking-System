from django.urls import path
from .views import IndexView, UserSignupView, UserLoginView, UserLogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
