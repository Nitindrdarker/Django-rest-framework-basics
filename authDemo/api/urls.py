from django.contrib import admin
from django.urls import path, include
from .views import TaskList, LoginView
urlpatterns = [
    path('', TaskList.as_view(), name='task-list')
]
