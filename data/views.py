from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import TaskSerializer
from django.views.decorators.cache import cache_page
# serializer importados
from .serializers import UserSerializer
from myapp.models import task
from django.core.cache import cache

class UserSession(APIView):
    serializer_class = UserSerializer
    def get(self,request):
        cache.set('signin', render(request,'signin.html'), timeout=120)
        return render(request,'signin.html')
    	
    def post(self, request,*args,**kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        AuthenticateUser = authenticate(username = username, password = password)
        if AuthenticateUser is None:
        	return render(request,'signin.html')
        login(request, AuthenticateUser)
        return redirect('home')

class CreateTask(generics.CreateAPIView):
    queryset = task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return redirect('home')
        else:
            return Response({'error': 'Hubo un error al intentar crear la tarea, intentelo de nuevo'})


