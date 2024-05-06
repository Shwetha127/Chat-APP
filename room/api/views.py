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
            queryset = queryset.filter(name=topic)
        return queryset


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    

class TopicList(generics.ListCreateAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    
