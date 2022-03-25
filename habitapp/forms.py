from socket import fromshare
from django import forms
from .models import User, Habit, Tracker

class HabitForm(forms.ModelForm):
    class Meta:
            model = Habit
            fields = [
                'goal',
                'description',
            ]

class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = [
            'habit',
            'daily_record',
            'goal_complete',
        ]
