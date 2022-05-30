from django.urls import path
from .views import Home,register,user_login,user_logout, user_profile
urlpatterns = [
    path('',Home, name='home'),
    path('register/',register, name='register'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('profile/<int:id>',user_profile, name='profile'),
]
