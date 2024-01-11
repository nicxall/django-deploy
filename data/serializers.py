from rest_framework import serializers
from django.contrib.auth.models import User
from myapp.models import task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ['title','description','important']