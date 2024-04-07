from django.urls import path
from .views import *

urlpatterns = [
    path("users/", UserAPIList.as_view()),
    path("users/<int:pk>", UserAPIDetailView.as_view()),
    path("clients/", ClientAPIList.as_view()),
    path("clients/<int:pk>", ClientAPIDetailView.as_view()),
    path("trainers/", TrainerAPIList.as_view()),
    path("trainers/<int:pk>", TrainerAPIDetailView.as_view()),
    path("gym-admins/", GymAdminAPIList.as_view()),
    path("gym-admins/<int:pk>", GymAdminAPIDetailView.as_view()),
]