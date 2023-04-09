from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link_1 = models.CharField(max_length=200)
    link_2 = models.CharField(max_length=200)
    link_3 = models.CharField(max_length=200)

    def __str__(self):
        return self.title