from rest_framework import generics
from .models import NewsArticle
from .serializers import NewsArticleSerializer

class NewsArticleListCreateView(generics.ListCreateAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
