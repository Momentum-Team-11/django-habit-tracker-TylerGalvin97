from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.text import slugify
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
    user = models.ForeignKey(User, related_name="habits", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tracker(models.Model):
    habit = models.ForeignKey(User, related_name="trackers", on_delete=models.CASCADE)
    daily_record = models.CharField(max_length=200)
    goal_complete = models.BooleanField(default=False)
    date_complete = models.DateField(auto_now_add=datetime.now)

    def __str__(self):
        return self.habit