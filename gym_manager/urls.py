from django.urls import path
from .views import *

urlpatterns = [
    path("gyms/", GymAPIList.as_view()),
    path("gyms/<int:pk>", GymAPIDetailView.as_view()),
    path("trainer-schedule/", TrainerScheduleAPIList.as_view()),
    path("trainer-schedule/<int:pk>", TrainerScheduleAPIDetailView.as_view()),
    path("client-schedule/", ClientScheduleAPIList.as_view()),
    path("client-schedule/<int:pk>", ClientScheduleAPIDetailView.as_view()),
]