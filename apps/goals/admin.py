from django.contrib import admin
from .models import Goal

class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'exercise', 'goal_type', 'target_value', 'deadline', 'is_achieved')
    search_fields = ('user__username', 'exercise__name', 'goal_type')
    list_filter = ('goal_type', 'is_achieved', 'exercise', 'deadline')
    ordering = ('deadline',)

admin.site.register(Goal, GoalAdmin)