from django.urls import path
from .views import WorshipScheduleView

urlpatterns = [
    path('worship-info/', WorshipScheduleView.as_view(),
         name='worship-info'),
]
