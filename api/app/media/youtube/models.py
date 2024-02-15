from django.db import models


class YoutubeVideo(models.Model):
    video_id = models.CharField(max_length=255, unique=True)
    thumbnail_url = models.URLField(max_length=500)
    fetched_date = models.DateTimeField(auto_now_add=True)
