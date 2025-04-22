from django.contrib import admin
from .models import Exercise

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'workout_program', 'sets', 'reps', 'rest_seconds')
    search_fields = ('name', 'description')
    list_filter = ('difficulty', 'workout_program')
    ordering = ('name',)
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'difficulty', 'workout_program', 'sets', 'reps', 'rest_seconds')
        }),
    )

admin.site.register(Exercise, ExerciseAdmin)