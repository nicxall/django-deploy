from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import UserGet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import JWTAuthentication

class UserData (viewsets.ModelViewSet):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]
    def get(self, request, *args,**kwargs):
		usuarios = User.object.all()
		serializers = UserGet(usuarios, many=True)
		return Response(serializers.data, status = status.HTTP_200_OK)

