from rest_framework import serializers
from exercise_api.models import Exercise, UNIT_CHOICES
'''
class ExerciseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    amount = serializers.IntegerField(default=1)
    sets = serializers.IntegerField(default=1)
    units = serializers.ChoiceField(choices=UNIT_CHOICES, default='reps')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Exercise.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.sets = validated_data.get('sets', instance.sets)
        instance.units = validated_data.get('units', instance.units)
        instance.save()
        return instance
'''

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'amount', 'sets', 'units')
