from django.urls import path
from .views import NewsArticleListCreateView

urlpatterns = [
    path('news/', NewsArticleListCreateView.as_view(), name='news_articles'),
]
