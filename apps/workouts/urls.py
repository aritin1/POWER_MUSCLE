from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WorkoutProgramViewSet

router = DefaultRouter()
router.register(r'workouts', WorkoutProgramViewSet, basename='workout')

urlpatterns = [
    path('', include(router.urls)),
]