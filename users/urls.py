from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import register,user_login,user_logout, user_profile

urlpatterns = [
    path('register/',register, name='register'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('profile/',user_profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
