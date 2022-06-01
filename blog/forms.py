from .models import Post

from django import forms

class UserPostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title','content', 'image', 'category', 'status')
        
        