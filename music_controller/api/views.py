from django.shortcuts import render
from rest_framework import generics
from .serialiserz import RoomSerializer
from .models import Room
# Create your views here.

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
