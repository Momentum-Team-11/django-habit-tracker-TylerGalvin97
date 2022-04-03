"""habit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from habitapp import views as habitapp_views
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path("", habitapp_views.home, name="home"),
    path("habit", habitapp_views.habit_list, name="habit_list"),
    path("habit/<int:pk>/", habitapp_views.habit_details,  name="habit_details"),
    # habit urls
    path("habit/add", habitapp_views.add_habit, name="add_habit"),
    path("habit/<int:pk>/edit/", habitapp_views.edit_habit, name="edit_habit"),
    path("habit/<int:pk>/delete/", habitapp_views.delete_habit, name="delete_habit"),
    # tracker urls 
    path("habit/<int:pk>/add/", habitapp_views.add_tracker, name="add_tracker"),
    path("habit/<int:pk>/edit/", habitapp_views.edit_tracker, name="edit_tracker"),
    path("habit/<int:pk>/delete/", habitapp_views.delete_tracker, name="delete_tracker"),
    # api urls
    path('api-auth/', include('rest_framework.urls')),
    path("api/habit", api_views.HabitListView.as_view(), name='api_habit_list'),
    path('api/habit/<int:pk>', api_views.HabitDetailsView.as_view(), name='api_habit_details'),
    path('api/habit/trackers', api_views.TrackerListView.as_view(), name='api_tracker_list'),
]
