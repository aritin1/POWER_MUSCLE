from django.db import models
from django.conf import settings
from apps.exercises.models import Exercise

class ExerciseStat(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='exercise_stats'
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='stats'
    )
    date = models.DateField(auto_now_add=True)
    sets_completed = models.PositiveIntegerField()
    reps_per_set = models.PositiveIntegerField()
    weight = models.FloatField(help_text="Вес в кг", null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name} on {self.date}"