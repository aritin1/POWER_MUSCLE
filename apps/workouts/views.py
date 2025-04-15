from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from apps.workouts.models import Author, Workout
from apps.workouts.serializers import WorkoutSerializer, AuthorSerializer, WorkoutCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend
class WorkoutListView(generics.ListAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'quantity', 'title']

class DetailView(generics.RetrieveAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class AuthorCreateView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class WorkoutCreateView(generics.CreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutCreateSerializer
