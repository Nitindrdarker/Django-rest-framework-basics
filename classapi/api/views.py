from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from .serilizer import TaskSerilizer
from rest_framework.response import Response
# Create your views here.


class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerilizer(tasks, many=True)
        return Response(serializer.data)

class TaskDetail(APIView):
    def get(self, request, pk):
        tasks = Task.objects.get(id=pk)
        serializer = TaskSerilizer(tasks, many=False)
        return Response(serializer.data)
class TaskPost(APIView):
    def post(self, request):
        serializer = TaskSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
class TaskUpdate(APIView):
    def post(self, request ,pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerilizer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
class TaskDelete(APIView):
    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return Response("Item deleted")
        
        