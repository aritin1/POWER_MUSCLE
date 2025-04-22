from rest_framework import generics, permissions
from .models import WorkoutProgram
from .serializers import WorkoutProgramSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class WorkoutProgramListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutProgramSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['level']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']

    def get_queryset(self):
        return WorkoutProgram.objects.filter(user=self.request.user)


class WorkoutProgramDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutProgram.objects.all()
    serializer_class = WorkoutProgramSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ограничим доступ только к своим программам
        return self.queryset.filter(user=self.request.user)