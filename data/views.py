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

# serializer importados
from .serializers import UserSerializer
from myapp.models import task

class UserSession(APIView):
    serializer_class = UserSerializer

    def get(self,request):
    	return render(request,'signin.html')
    	
    def post(self, request,*args,**kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        AuthenticateUser = authenticate(username = username, password = password)
        if AuthenticateUser is None:
        	return render(request,'signin.html')
        login(request, AuthenticateUser)
        return redirect('home')


class CreateTask(APIView):
    # Define el conjunto de objetos sobre el que operará la vista
    queryset = Task.objects.all()
    # Especifica el serializador que se utilizará para validar y deserializar datos
    serializer_class = UserSerializer

    # Este método se llama automáticamente cuando se crea un nuevo objeto
    @action(detail=False, action='post')
    def perform_create(self, serializer):
        # Guarda el objeto serializado en la base de datos, asignando el usuario actual
        serializer.save(user=self.request.user)
        # Redirige a la vista 'home' después de guardar el objeto
        return redirect('home')


