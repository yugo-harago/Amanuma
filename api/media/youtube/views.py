from django.http import JsonResponse
from rest_framework.views import APIView
import requests
from django.conf import settings
from .models import YoutubeVideo
from django.utils import timezone
from .serializers import YoutubeVideoSerializer


class GoogleApiView(APIView):

    def get(self, request, *args, **kwargs):
        videos = YoutubeVideo.objects.order_by('-fetched_date')[:5]
        serializer = YoutubeVideoSerializer(videos, many=True)
        return JsonResponse(serializer.data, safe=False)

    def patch(self, request, *args, **kwargs):
        key = settings.YOUTUBE_API_KEY
        response = requests.get(
            f'https://www.googleapis.com/youtube/v3/search?key={key}&channelId=UCyGi650LKtPYxZpySw3C_ag&part=snippet,id&order=date&maxResults=5')
        data = response.json()

        for item in data['items']:
            video_id = item['id']['videoId']
            thumbnail_url = item['snippet']['thumbnails']['default']['url']
            YoutubeVideo.objects.update_or_create(
                video_id=video_id,
                defaults={'thumbnail_url': thumbnail_url,
                          'fetched_date': timezone.now()},
            )

        return JsonResponse(data, safe=False)
