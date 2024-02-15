from django.db import models
from django.contrib.auth.models import User

from enum import Enum

class ChatSourceType(Enum):
    EMAIL = 'email'
    LINE = 'line'
    WEB = 'web'

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    source = models.CharField(
        max_length=10,
        choices=[(source_type.value, source_type.name) for source_type in ChatSourceType],
        default=ChatSourceType.EMAIL.value
    )

    def __str__(self):
        return f'{self.author.username}: {self.content}'
