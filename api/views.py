from rest_framework.views import APIView
from rest_framework.response import Response
from habitapp.models import Habit, Tracker
from .serializer import HabitSerializer, HabitTrackerSerializer, TrackerSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView 

class HabitListView(ListAPIView):
  queryset = Habit.objects.all()
  serializer_class = HabitSerializer

class HabitDetailsView(RetrieveUpdateDestroyAPIView):
  queryset = Habit.objects.all()
  serializer_class = HabitTrackerSerializer

class TrackerListView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
  queryset = Tracker.objects.all()
  serializer_class = TrackerSerializer




    # def get(self, request, format=None):
    #     """
    #     List all the habits 
    #     """
    #     habits = Habits.objects.all()
    #     serializer = HabitSerializer(habits, many=True)
    #     return Response(serializer.data)


    #queryset
    #serializer
    #optionally permissions
    #return a response with json data
