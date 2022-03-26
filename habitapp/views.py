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

def habit_details(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    result = Tracker.objects.filter(habit=habit.id)
    return render (request, "habit_details.html", {'habit': habit, 'result' : result})

    # add edit delete habits

def add_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='habit_list')
    return render (request, "add_habit.html", {'form': form})

def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='habit_list')
    return render (request, "edit_habit.html", {'form': form, 'habit': habit})

def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='habit_list')
    return render (request, "delete_habit.html", {'habit': habit})

    #  add edit delete trackers

def add_tracker(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = TrackerForm()
    else:
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='habit_list')
    return render (request, "add_tracker.html", {'form': form, 'habit': habit})

def edit_tracker(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=tracker)
    else:
        form = HabitForm(data=request.POST, instance=tracker)
        if form.is_valid():
            form.save()
            return redirect(to='habit_list')
    return render (request, "edit_tracker.html", {'form': form, 'tracker': tracker})

def delete_tracker(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    if request.method =="POST":
        tracker.delete()
        return redirect(to="habit_list")
    return render (request, "delete_habit.html", {"tracker": tracker})