from django.contrib import admin

# Register your models here.
from .models import Post,PostView,Like,Comment
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Like)
admin.site.register(Comment)
