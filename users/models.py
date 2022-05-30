from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    portfolio = models.URLField(blank=True) #! blank true yani birşey girmezse hata verme.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #! on_delete=models.CASCADE = kullanici silinirse usersprofile sayfasındakılerde sılınsın.
    def __str__(self):
        return self.user.username
