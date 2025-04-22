from django.contrib import admin
from .models import ExerciseStat

class ExerciseStatAdmin(admin.ModelAdmin):
    list_display = ('user', 'exercise', 'date', 'sets_completed', 'reps_per_set', 'weight')
    search_fields = ('user__username', 'exercise__name', 'date')
    list_filter = ('exercise', 'date', 'user')
    ordering = ('-date',)

admin.site.register(ExerciseStat, ExerciseStatAdmin)