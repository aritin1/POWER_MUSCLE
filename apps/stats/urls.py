from django.urls import path
from .views import ExerciseStatListCreateView, ExerciseStatDetailView

urlpatterns = [
    path('', ExerciseStatListCreateView.as_view(), name='stat_list_create'),
    path('<int:pk>/', ExerciseStatDetailView.as_view(), name='stat_detail'),
]