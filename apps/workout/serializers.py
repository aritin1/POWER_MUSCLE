from rest_framework import serializers
from .models import Workout, WorkoutExercise, Set

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ['id', 'repetitions', 'weight', 'rpe']

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    sets = SetSerializer(many=True)
    exercise_name = serializers.CharField(source='exercise.name', read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = ['id', 'exercise', 'exercise_name', 'order', 'sets']

    def create(self, validated_data):
        sets_data = validated_data.pop('sets')
        workout_exercise = WorkoutExercise.objects.create(**validated_data)
        for set_data in sets_data:
            Set.objects.create(workout_exercise=workout_exercise, **set_data)
        return workout_exercise

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(many=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'name', 'date', 'notes', 'exercises']
        read_only_fields = ['user']

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        workout = Workout.objects.create(user=self.context['request'].user, **validated_data)
        for exercise_data in exercises_data:
            sets_data = exercise_data.pop('sets')
            workout_exercise = WorkoutExercise.objects.create(workout=workout, **exercise_data)
            for set_data in sets_data:
                Set.objects.create(workout_exercise=workout_exercise, **set_data)
        return workout