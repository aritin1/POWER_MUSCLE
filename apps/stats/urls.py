from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseStatViewSet

router = DefaultRouter()
router.register(r'stats', ExerciseStatViewSet, basename='exercise-stat')

urlpatterns = [
    path('', include(router.urls)),
]
