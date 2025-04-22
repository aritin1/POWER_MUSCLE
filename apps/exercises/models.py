from django.db import models
from apps.workouts.models import WorkoutProgram

class Exercise(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    workout_program = models.ForeignKey(
        WorkoutProgram,
        on_delete=models.CASCADE,
        related_name='exercises'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    rest_seconds = models.PositiveIntegerField(help_text="Отдых между подходами в секундах")

    def __str__(self):
        return f"{self.name} ({self.difficulty})"