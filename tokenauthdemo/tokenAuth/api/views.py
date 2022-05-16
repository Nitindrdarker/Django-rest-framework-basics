from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serilizer import TaskSerilizer, UserSerilizer
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.contrib.auth.models import User




class HelloView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Task.objects.all()
    serializer_class = TaskSerilizer

class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerilizer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'error':serializer.errors, "message":'some errors'})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        # print(user)
        token_obj, _ = Token.objects.get_or_create(user=user)
        return Response({'status':200, 'payload':serializer.data, 'token':str(token_obj)})



