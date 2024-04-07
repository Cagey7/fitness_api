from rest_framework import generics
from .models import *
from .serializers import *


class GymAPIList(generics.ListCreateAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


class GymAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


class TrainerScheduleAPIList(generics.ListCreateAPIView):
    queryset = TrainerSchedule.objects.all()
    serializer_class = TrainerScheduleSerializer


class TrainerScheduleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainerSchedule.objects.all()
    serializer_class = TrainerScheduleSerializer


class ClientScheduleAPIList(generics.ListCreateAPIView):
    queryset = ClientSchedule.objects.all()
    serializer_class = ClientScheduleSerializer


class ClientScheduleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientSchedule.objects.all()
    serializer_class = ClientScheduleSerializer
