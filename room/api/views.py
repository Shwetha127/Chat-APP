from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import generics

from room.models import Room, Topic
from .serializers import RoomSerializer, TopicSerializer



class RoomList(generics.ListCreateAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = Room.objects.all()
        topic = self.request.query_params.get('topic')
        if topic is not None:
            queryset = queryset.filter(topic=topic)
        return queryset


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
