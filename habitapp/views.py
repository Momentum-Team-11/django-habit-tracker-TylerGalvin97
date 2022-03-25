from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Habit, Tracker
from django.contrib.auth.decorators import login_required
from .forms import HabitForm, TrackerForm
import datetime


def home(request):
    if request.user.is_authenticated:
        return redirect("habit_list")
    return render(request,"home.html")

@login_required
def habit_list(request):
    habits = Habit.objects.all()
    return render(request, "habit_list.html", {"habits": habits})