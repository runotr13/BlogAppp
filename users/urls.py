from django.urls import path
from .views import Home,register,user_login
urlpatterns = [
    path('',Home, name='home'),
    path('register/',register, name='register'),
    path('login/',user_login, name='login'),
]