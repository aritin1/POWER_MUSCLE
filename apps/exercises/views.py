from rest_framework import generics, permissions
from .models import Exercise
from .serializers import ExerciseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ExerciseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['difficulty']
    search_fields = ['name', 'description']

    def get_queryset(self):
        return Exercise.objects.filter(workout_program__user=self.request.user)


class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Exercise.objects.filter(workout_program__user=self.request.user)