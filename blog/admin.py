from django.contrib import admin
from .models import Post, Comment, Profile

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "author",)
admin.site.register(Post, PostAdmin)
class CommentAdmin(admin.ModelAdmin):
	list_display = ("content", "author",)
admin.site.register(Comment, CommentAdmin)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ("name", "surname",)
admin.site.register(Profile, ProfileAdmin)
