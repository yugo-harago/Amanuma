from rest_framework import serializers
from .models import YoutubeVideo


class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = ['video_id', 'thumbnail_url', 'fetched_date', 'title']
