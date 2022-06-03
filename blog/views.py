from django.shortcuts import redirect, render
from .forms import UserPostForm,CommentForm
from .models import Post,PostView,Like,Comment
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
    for post in postlist:
        post.comment_count = Comment.objects.filter(post_id = post.id).count()
        post.view_count = PostView.objects.filter(post_id = post.id).count()
        post.like_count = Like.objects.filter(post_id = post.id).count()
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
            return redirect('postDetail', id=id)
    else:
        messages.error(request, 'You are not allowed to delete this post')
        return redirect('post_detail', id=id)
    context = {
        "post": post,
    }
    return render(request, 'blog/post_delete.html', context)


def post_detail(request,id):
    post = Post.objects.get(pk=id)
    # forms = UserPostForm(instance=post)
    comment_form = CommentForm()
    list_comment = Comment.objects.filter(post=post)
    # post.view_count = post.view_count +1
    # post.save()
    viewList = PostView.objects.create(post=post)
    viewList.save()
    viewCount = PostView.objects.filter(post=post)
    like_count = Like.objects.filter(post=post)

    if request.method == 'POST':
        # form = UserPostForm(request.POST,request.FILES,instance=post)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comments = comment_form.save(commit=False)
            comments.user = request.user
            comments.post = post
            comments.save()

            messages.success(request,'You Comment Success!')
            return redirect('postDetail', id=id)
    context = {
        "comment_form" : comment_form,
        "post" : post,
        "viewCount" : viewCount,
        "like_count" : like_count,
        "list_comment" : list_comment
    }
    return render(request,'blog/post_detail.html',context)


def add_like(request,id):
    post = Post.objects.get(pk=id)
    check_like = Like.objects.filter(user=request.user,post=post)
    if not check_like :
        like_list = Like.objects.create(user=request.user,post=post)
        like_list.save()
    else:
        check_like.delete()
    return redirect('postDetail',id=id)

