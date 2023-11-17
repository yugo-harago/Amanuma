from django.db import models
from django.db.models import JSONField


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True)
    links = JSONField(null=True)

    def __str__(self):
        return self.title
