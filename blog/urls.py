from django.urls import path
from .views import posts, profile, addLike, comments, likes, addComment, blockedUsers

urlpatterns = [
    path('', posts, name="posts"),
    path('profile/', profile, name="profile"),
    path('like/<int:pk>', addLike, name="like"),
    path('comments/<int:pk>', comments, name="comments"),
    path('viewlike/<int:pk>', likes, name="view_likes"),
    path('addComment/<int:pk>', addComment, name="add_comment"),
    path('blocked-users/', blockedUsers, name="blocked_users"),
    #path('unblock-user/<int:pk>', unblockUser, name="unblock_user")
]