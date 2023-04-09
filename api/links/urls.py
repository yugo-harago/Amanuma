from django.urls import path
from .views import UsefulLinkListCreateView

urlpatterns = [
    path('links/', UsefulLinkListCreateView.as_view(), name='useful_links'),
]
