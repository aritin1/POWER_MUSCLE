from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import ExerciseStat
from .serializers import ExerciseStatSerializer

class ExerciseStatViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseStatSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['exercise', 'date']
    ordering_fields = ['date', 'weight', 'sets_completed']

    def get_queryset(self):
        return ExerciseStat.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)