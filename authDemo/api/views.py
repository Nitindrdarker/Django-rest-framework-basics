from django.shortcuts import render
from django.urls import reverse_lazy


# Create your views here.
from rest_framework.views import APIView
from .models import Task
from .serializer import TaskSerilizer
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.views import LoginView
from rest_framework import generics





class TaskList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerilizer
    name = 'task-list'