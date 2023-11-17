from django.urls import path
from .views import ArticleListCreateView

urlpatterns = [
    path('article/', ArticleListCreateView.as_view(), name='articles'),
    path('article/<int:pk>/', ArticleListCreateView.as_view(), name='article-detail'),
]
