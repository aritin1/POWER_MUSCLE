from django.contrib import admin
from .models import WorkoutProgram

class WorkoutProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'user', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('level', 'user', 'created_at')
    ordering = ('-created_at',)

admin.site.register(WorkoutProgram, WorkoutProgramAdmin)