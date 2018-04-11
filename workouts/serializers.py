from rest_framework import serializers
from workouts.models import Exercise, Set, Session, UNIT_CHOICES

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('title', 'exercise_slug')

        
class SetSerializer(serializers.ModelSerializer):
    # How do I make this list the name of the exercise and not the pk?
    exercise = serializers.SlugRelatedField(
        read_only=True,
        many=False,
        slug_field='title')

    class Meta:
        model = Set
        fields = ('exercise', 'amount', 'units')


class SessionSerializer(serializers.ModelSerializer):
    sets = SetSerializer(read_only=True, many=True)
    class Meta:
        model = Session
        fields = ('created', 'title', 'sets')
