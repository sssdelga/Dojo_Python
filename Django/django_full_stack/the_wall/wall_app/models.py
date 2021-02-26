from django.db import models
from login_app.models import User

class Message(models.Model):
    author = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    message_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    author = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='message_comments', on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)