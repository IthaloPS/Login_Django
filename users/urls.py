from django.urls import path, include
from users import views
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('home/', views.home, name='home'),
    path('logout_user/', views.logout_user, name='logout_user')
]
