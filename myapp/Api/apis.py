from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import UserGet

class UserData (viewsets.ModelViewSet):

    def get(self, request):
    	user = request.user
    	serializer = UserGet(user)
    	return Response(serializer.data)
