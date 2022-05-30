from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
# Create your models here.
class UserProfile(models.Model):
    portfolio = models.URLField(blank=True) #! blank true yani birşey girmezse hata verme.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #! on_delete=models.CASCADE = kullanici silinirse usersprofile sayfasındakılerde sılınsın.
    def __str__(self):
        return self.user.username


class UserProfiletwo(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    Image = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.username

