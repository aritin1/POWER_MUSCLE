from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from apps.workouts.models import WorkoutProgram
from apps.exercises.models import Exercise
from apps.exercises.serializers import ExerciseSerializer
from apps.workouts.serializers import WorkoutProgramSerializer

import random

class GenerateWorkoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        level = request.data.get('level')
        title = request.data.get('title', f"Авто-программа ({level})")

        if level not in ['beginner', 'intermediate', 'advanced']:
            return Response({'error': 'Неверный уровень сложности'}, status=400)

        # Список подходящих упражнений
        suitable_exercises = Exercise.objects.filter(difficulty__in=self._map_level(level))

        if not suitable_exercises.exists():
            return Response({'error': 'Нет доступных упражнений для этого уровня'}, status=404)

        # Создание программы
        program = WorkoutProgram.objects.create(
            user=request.user,
            title=title,
            level=level,
            description="Сгенерировано автоматически"
        )

        # Привязка случайных упражнений к новой программе
        selected = random.sample(list(suitable_exercises), min(5, suitable_exercises.count()))
        for exercise in selected:
            exercise.pk = None  # копируем
            exercise.workout_program = program
            exercise.save()

        return Response({
            'message': 'Программа создана',
            'program': WorkoutProgramSerializer(program).data,
            'exercises': ExerciseSerializer(program.exercises.all(), many=True).data
        }, status=status.HTTP_201_CREATED)

    def _map_level(self, level):
        return {
            'beginner': ['easy'],
            'intermediate': ['easy', 'medium'],
            'advanced': ['medium', 'hard']
        }[level]