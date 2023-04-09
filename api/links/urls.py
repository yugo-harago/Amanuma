from django.urls import path
from .views import LinkListCreateView

urlpatterns = [
    path('links/', LinkListCreateView.as_view(), name='useful_links'),
]
