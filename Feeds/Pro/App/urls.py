from django.urls import path
from .views import feed, post_message,message_list,post_comment,delete_message,like_message,like_comment

urlpatterns = [
    path('feed/', feed, name='feed'),
    path('post_message/', post_message, name='post_message'),
    path('', message_list, name='message_list'),
    path('post_comment/', post_comment, name='post_comment_without_id'),
    path('post_comment/<int:message_id>/', post_comment, name='post_comment'),
    path('delete_message/<int:message_id>/', delete_message, name='delete_message'),
    path('like_message/<int:message_id>/', like_message, name='like_message'),
    path('like_comment/<int:comment_id>/', like_comment, name='like_comment'),
]

