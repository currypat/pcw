from rest_framework import serializers
from workouts.models import Exercise, Set, Session, UNIT_CHOICES

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('title', 'exercise_slug')

        
class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ('exercise', 'amount', 'units')


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('created', 'title', 'sets')
