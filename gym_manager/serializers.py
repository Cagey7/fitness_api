from rest_framework import serializers
from .models import *


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = "__all__"


class TrainerScheduleSerializer(serializers.ModelSerializer):    
    class Meta:
        model = TrainerSchedule
        fields = "__all__"


class ClientScheduleSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ClientSchedule
        fields = "__all__"
