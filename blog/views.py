from django.shortcuts import redirect, render
from .forms import UserPostForm
from .models import Post
from django.contrib import messages
# Create your views here.
def post_create(request):
    form = UserPostForm()
    
    if request.method == 'POST':
        form = UserPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "You Post Success!")
            return redirect('list')
    context = {
        'form' : form
    }
    return render(request,'blog/post_create.html',context)


def post_list(request):
    postlist = Post.objects.all()

    context = {
        "list" : postlist
    }
    return render(request,'blog/post_list.html',context)


def post_update(request,id):
    post = Post.objects.get(pk=id)
    form = UserPostForm(instance=post)
    if post.user == request.user:
        if request.method == 'POST':
            form = UserPostForm(request.POST,request.FILES,instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,'You Updated Success!')
                return redirect('list')
            else:
                messages.error(request,'You are not allowed to updated this post')
                return redirect('update')

    context = {
        "form" : form,
        'post' : post
    }
    return render(request,'blog/post_update.html',context)




def post_delete(request, id):
    post = Post.objects.get(id=id)
    if post.user == request.user:
        if request.method == "POST":
            post.delete()
            messages.success(request, 'Post deleted successfully')
            return redirect('list')
    else:
        messages.error(request, 'You are not allowed to delete this post')
        return redirect('post_detail', id=id)
    context = {
        "post": post,
    }
    return render(request, 'blog/post_delete.html', context)
