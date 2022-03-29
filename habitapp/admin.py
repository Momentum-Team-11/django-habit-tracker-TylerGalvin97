from django.contrib import admin
from .models import User, Habit, Tracker

admin.site.register(User)
admin.site.register(Habit)
admin.site.register(Tracker)

# Register your models here.
