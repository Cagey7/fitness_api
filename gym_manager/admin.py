from django.contrib import admin
from .models import Gym, TrainerSchedule, ClientSchedule


@admin.register(Gym)
class GymsAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "gym_admin"]


@admin.register(TrainerSchedule)
class TrainerScheduleAdmin(admin.ModelAdmin):
    list_display = ["week_day", "start_time", "end_time", "gym", "trainer"]


@admin.register(ClientSchedule)
class ClientScheduleAdmin(admin.ModelAdmin):
    list_display = ["date", "start_time", "end_time", "gym", "trainer", "client"]
