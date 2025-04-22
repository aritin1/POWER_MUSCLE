from rest_framework import serializers
from .models import WorkoutProgram

class WorkoutProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutProgram
        fields = '__all__'
        read_only_fields = ('user', 'created_at')