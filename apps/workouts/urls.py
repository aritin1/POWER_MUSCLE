from django.urls import path
from .views import WorkoutProgramListCreateView, WorkoutProgramDetailView

urlpatterns = [
    path('', WorkoutProgramListCreateView.as_view(), name='workout_list_create'),
    path('<int:pk>/', WorkoutProgramDetailView.as_view(), name='workout_detail'),
]
