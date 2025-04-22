from django.urls import path
from .views import ExerciseListCreateView, ExerciseDetailView

urlpatterns = [
    path('', ExerciseListCreateView.as_view(), name='exercise_list_create'),
    path('<int:pk>/', ExerciseDetailView.as_view(), name='exercise_detail'),
]