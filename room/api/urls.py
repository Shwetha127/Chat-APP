from django.urls import path
from .views import RoomList, RoomDetail, TopicDetail, TopicList

urlpatterns = [
    path('topic/', TopicList.as_view()),
    path('topic/<int:pk>/', TopicDetail.as_view()),
    path('room/', RoomList.as_view()),
    path('room/<int:pk>/', RoomDetail.as_view()),
]