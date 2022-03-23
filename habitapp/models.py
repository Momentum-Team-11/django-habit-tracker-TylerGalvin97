from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=250)
    goal = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title