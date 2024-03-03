from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes = models.ManyToManyField('Like', related_name='liked_comments', blank=True)
    message = models.ForeignKey('Message', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey('Message', on_delete=models.CASCADE, related_name='likes')
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='likes', blank=True, null=True)


class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # comments = models.ManyToManyField('Comment', related_name='message_likes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


class LikeComment(models.Model):
    # Other fields...

    # Assuming ForeignKey to Message model
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE)
