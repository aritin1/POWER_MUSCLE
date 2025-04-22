from rest_framework import generics, permissions
from .models import WorkoutProgram
from .serializers import WorkoutProgramSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets


class WorkoutProgramViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutProgramSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['level']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']

    def get_queryset(self):
        return WorkoutProgram.objects.filter(user=self.request.user)