from django.urls import path
from .views import GenerateWorkoutView

urlpatterns = [
    path('generate/', GenerateWorkoutView.as_view(), name='generate_workout')
]