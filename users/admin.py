from django.contrib import admin
from .models import User, Trainer, Client, GymAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "middle_name", "gender", "date_of_birth")
    list_filter = ("gender", "date_of_birth")
    search_fields = ("username", "email", "first_name", "last_name", "middle_name")


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(GymAdmin)
class GymAdminAdmin(admin.ModelAdmin):
    list_display = ("user",)
