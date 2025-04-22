from django.contrib import admin
from .models import Exercise

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'workout_program', 'sets', 'reps', 'rest_seconds')  # Указываем только существующие поля
    search_fields = ('name', 'description')  # Поиск по имени и описанию
    list_filter = ('difficulty', 'workout_program')  # Фильтрация по сложности и тренировочной программе
    ordering = ('name',)  # Сортировка по имени упражнения
    list_per_page = 20  # Пагинация на 20 объектов на странице

    # Настройка форм
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'difficulty', 'workout_program', 'sets', 'reps', 'rest_seconds')
        }),
    )

admin.site.register(Exercise, ExerciseAdmin)