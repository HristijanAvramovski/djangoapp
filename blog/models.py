from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200, blank=True, null=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField(blank=True, null=True)
    file=models.FileField(blank=True, null=True)
    dateCreated=models.DateTimeField(auto_now_add=True)
    lastChange=models.DateTimeField(auto_now=True)
    likes=models.ManyToManyField(User, related_name="likes")

    def __str__(self):
        return self.title

    def count_likes(self):
        return self.likes.count()

class Comment(models.Model):
    content=models.TextField()
    post=models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Profile(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="cover_images/", blank=True, null=True)
    intrests=models.TextField(blank=True, null=True)
    skills=models.TextField(blank=True, null=True)
    profession=models.TextField(blank=True, null=True)
    blocked_users=models.ManyToManyField(User, related_name="blocked_users")

    def __str__(self):
        return self.name + " "+self.surname