from rest_framework import serializers
from .models import ExerciseStat

class ExerciseStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseStat
        fields = '__all__'
        read_only_fields = ('user', 'date')