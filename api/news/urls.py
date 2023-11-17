from django.urls import path
from .views import NewsListCreateView

urlpatterns = [
    path('news/', NewsListCreateView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsListCreateView.as_view(), name='news-detail'),
]
