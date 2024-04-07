from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "М", "Мужчина"
        FEMALE = "Ж", "Женщина"
        OTHER = "Д", "Другое"

    middle_name = models.CharField(max_length=127, null=True, default=None, blank=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, null=True, default=None, blank=True)
    date_of_birth = models.DateField(null=True, default=None, blank=True)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trainers = models.ManyToManyField("Trainer", through="gym_manager.ClientSchedule")
    height = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(100), MaxValueValidator(250)])
    weight = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(20), MaxValueValidator(300)])

    def __str__(self):
        return f"Клиент: {self.user.last_name} {self.user.first_name}"


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gyms = models.ManyToManyField("gym_manager.Gym", through="gym_manager.TrainerSchedule")
    price_per_hour = models.IntegerField(null=True, blank=True)
    specialization = models.CharField(max_length=511, null=True, blank=True)
    
    def __str__(self):
        return f"Тренер: {self.user.last_name} {self.user.first_name}"


class GymAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Админ зала: {self.user.last_name} {self.user.first_name}"
