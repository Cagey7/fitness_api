from rest_framework import generics
from .models import *
from .serializers import *


class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientAPIList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TrainerAPIList(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class TrainerAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class GymAdminAPIList(generics.ListCreateAPIView):
    queryset = GymAdmin.objects.all()
    serializer_class = GymAdminSerializer


class GymAdminAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GymAdmin.objects.all()
    serializer_class = GymAdminSerializer
