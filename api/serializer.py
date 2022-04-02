from habitapp.models import Habit, Tracker, User
from rest_framework import serializers

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'pk',
            'user',
            'goal',
            'description',
            'start',
        )

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = (
            'pk',
            'habit',
            'daily_record',
            'goal_complete',
            'date_created',
        )

class HabitTrackerSerializer(serializers.ModelSerializer):
    records = TrackerSerializer(many=True, required=False, source='habits')
    class Meta:
        model = Habit
        fields = (
            'pk',
            'name',
            'tracker',
        )