from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task
class TaskSerilizer(serializers.ModelSerializer):
    class Meta():
        model = Task
        fields = '__all__'


class UserSerilizer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user