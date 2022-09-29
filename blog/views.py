from django.shortcuts import render, redirect
from .models import Post, Profile, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User


# Create your views here.
def posts(request):
    if request.method == "POST":
        form_data=PostForm(data=request.POST)
        if form_data.is_valid():
            post=form_data.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("/posts")
    posts=Post.objects.all()
    profiles=Profile.objects.all()
    profile=Profile.objects.get(user=request.user)
    blockedUsers=profile.blocked_users.all
    return render(request, "posts.html", {"posts":posts,"form":PostForm, "profiles":profiles, "blockedUsers":blockedUsers})

def profile(request):
    userProfile=Profile.objects.get(user=request.user)
    user=request.user
    posts=Post.objects.filter(author=request.user)
    return render(request, "profile.html", {"userProfile":userProfile,"user":user,"posts":posts})

def addLike(request, pk):
    post=Post.objects.get(id=pk)
    post.likes.add(request.user)
    return redirect("/posts")

def comments(request,pk):
    
    post=Post.objects.get(id=pk)
    comments=post.comments.all
    return render(request,"comments.html",{"comments":comments,"post":post})

def likes(request, pk):
    post=Post.objects.get(id=pk)
    likes=post.likes.all
    return render(request, "likes.html", {"likes":likes})

def addComment(request, pk):
    content=request.POST.get("content")
    post=Post.objects.get(id=pk)
    user=request.user
    comment=Comment(content=content, post=post, author=user)
    comment.save()
    return redirect("/posts")

def blockedUsers(request):
    user=Profile.objects.get(user=request.user)
    blockedUsers=user.blocked_users.all
    return render(request, "blocked_users.html", {"blockedUsers":blockedUsers})

#def unblockUser(request, pk):
    userId=request.user
    profile=Profile.objects.get(user=userId)
    profile.blocked_users.remove(pk)
    return redirect("/posts/blocked-users")
