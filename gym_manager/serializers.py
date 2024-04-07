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

    def validate(self, attrs):
        start_time = attrs.get("start_time")
        end_time = attrs.get("end_time")

        time_difference = (end_time.hour * 60 + end_time.minute) - (start_time.hour * 60 + start_time.minute)
        if time_difference < 60:
            raise serializers.ValidationError("Можно записаться минимум на час")
        
        weekday_mapping = {0: "ПН", 1: "ВТ", 2: "СР", 3: "ЧТ", 4: "ПТ", 5: "СБ", 6: "ВС"}
        day_input = weekday_mapping[attrs["date"].weekday()]
        trainer_schedule = TrainerSchedule.objects.filter(trainer=attrs["trainer"], week_day=day_input).first()
        if not trainer_schedule:
            raise serializers.ValidationError("В этот день тренер не работает")

        if not (trainer_schedule.start_time <= start_time < end_time <= trainer_schedule.end_time):
            raise serializers.ValidationError(f"Выберите время в диапазоне времени работы тренера {trainer_schedule.start_time} - {trainer_schedule.end_time}")

        client_schedules = ClientSchedule.objects.filter(trainer=attrs["trainer"], date=attrs["date"])
        for client_schedule in client_schedules:
            if client_schedule.start_time <= start_time < end_time <= client_schedule.end_time:
                raise serializers.ValidationError("Это время уже занято")

        return attrs
