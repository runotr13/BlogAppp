
from .models import Post,Comment
from django import forms

class UserPostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title','content', 'image', 'category', 'status')
    

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('content',)