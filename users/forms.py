
from dataclasses import fields
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username','email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile 
        exclude = ('user',) #! exclude ile user istemiyoruz diyouz !!!

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email')