from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    POST_CATEGORY_CHOİCES = [
        ('FS','Full Stack'),
        ('DS','Data Science'),
        ('AWS','Amazon Web Services'),
    ]
    category = models.CharField(max_length=3, choices=POST_CATEGORY_CHOİCES, default='FS')
    POST_STATUS_CHOİCES = [
        ('D','Draft'),
        ('P','Published'),
    ]
    status = models.CharField(max_length=2, choices=POST_STATUS_CHOİCES, default='D')
    comment_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.title} by {self.user.username}"

class PostView(models.Model):
    timeStamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"[ {self.timeStamp} ] POST TITLE=> {self.post.title} "


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[ {self.user} ] POST TITLE=> {self.post.title} "

class Comment(models.Model):
    timeStamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post.title    

