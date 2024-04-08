from rest_framework import serializers
from .models import *
from gym_manager.serializers import GymSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    trainers = TrainerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Client
        fields = "__all__"

class GymAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymAdmin
        fields = "__all__"
