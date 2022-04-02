from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint
from datetime import datetime

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

# Create your models here.
class Habit(models.Model):
    goal = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, related_name="habits", on_delete=models.CASCADE, null=True, blank=True)
    start = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.goal

class Tracker(models.Model):
    habit = models.ForeignKey(Habit, related_name="trackers", on_delete=models.CASCADE, null=True, blank=True)
    daily_record = models.CharField(max_length=200)
    goal_complete = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['habit', 'date_created'], name='one_record_per_day')
        ]

    def __str__(self):
        return str(self.daily_record)
    