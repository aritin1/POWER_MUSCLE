from rest_framework import serializers

from .models import Author, Workout


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class WorkoutSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Workout
        fields = [
            'id',
            'title',
            'quantity',
            'author'
        ]

class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id'
        ]
class WorkoutCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    class Meta:
        model = Workout
        fields = [
            'id',
            'title',
            'quantity',
            'author'
        ]