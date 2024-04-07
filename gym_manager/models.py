from django.db import models
from django.core.exceptions import ValidationError
from users.models import Trainer, Client, GymAdmin


class Gym(models.Model):
    name = models.CharField(max_length=127)
    address = models.CharField(max_length=511)
    gym_admin = models.ForeignKey(GymAdmin, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"


class TrainerSchedule(models.Model):
    class DayOfTheWeek(models.TextChoices):
        MONDAY = "ПН", "Понедельник"
        TUESDAY = "ВТ", "Вторник"
        WEDNESDAY = "СР", "Среда"
        THURSDAY = "ЧТ", "Четверг"
        FRIDAY = "ПТ", "Пятница"
        SATURDAY = "СБ", "Суббота"
        SUNDAY = "ВС", "Воскресенье"

    week_day = models.CharField(max_length=2, choices=DayOfTheWeek.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    gym = models.ForeignKey(Gym, on_delete=models.SET_NULL, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ("trainer", "week_day")


class ClientSchedule(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    gym = models.ForeignKey(Gym, on_delete=models.SET_NULL, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
