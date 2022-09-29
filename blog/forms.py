from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=("author","likes",)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=('author',)