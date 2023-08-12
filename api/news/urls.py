from django.urls import path
from .views import ArticleListCreateView

urlpatterns = [
    path('news/', ArticleListCreateView.as_view(), name='news_articles'),
    path('news/<int:pk>/', ArticleListCreateView.as_view(), name='article-detail'),
]
