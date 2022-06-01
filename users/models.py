from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
# Create your models here.
class UserProfile(models.Model):
    profile_pics = models.ImageField(upload_to='profile_pics', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True) #! blank true yani birşey girmezse hata verme.
    #! on_delete=models.CASCADE = kullanici silinirse usersprofile sayfasındakılerde sılınsın.
    def __str__(self):
        return self.user.username


