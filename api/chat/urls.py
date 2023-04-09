from django.urls import path
from .views import MessageListCreateView, ChatRoomListCreateView, ChatRoomRetrieveUpdateDestroyView

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='messages'),
    path('chatrooms/', ChatRoomListCreateView.as_view(), name='chatrooms'),
    path('chatrooms/<int:pk>/', ChatRoomRetrieveUpdateDestroyView.as_view(), name='chatroom-detail'),
]
