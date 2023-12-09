from django.http import JsonResponse
from rest_framework.views import APIView
import requests
from django.conf import settings


class GoogleApiView(APIView):
    def get(self, request, *args, **kwargs):
        key = settings.YOUTUBE_API_KEY
        response = requests.get(
            f'https://www.googleapis.com/youtube/v3/search?key={key}&channelId=UCyGi650LKtPYxZpySw3C_ag&part=snippet,id&order=date&maxResults=5')
        return JsonResponse(response.json(), safe=False)
