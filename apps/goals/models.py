from django.db import models
from django.conf import settings
from apps.exercises.models import Exercise

class Goal(models.Model):
    GOAL_TYPES = (
        ('reps', 'Повторы'),
        ('weight', 'Вес'),
        ('consistency', 'Регулярность'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='goals'
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='goals'
    )
    goal_type = models.CharField(max_length=20, choices=GOAL_TYPES)
    target_value = models.FloatField(help_text="Целевое значение (в зависимости от типа)")
    deadline = models.DateField()
    is_achieved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.exercise.name}: {self.goal_type} до {self.deadline}"