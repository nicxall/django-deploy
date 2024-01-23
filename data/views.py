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

class AuthenticationViewFactory:
    @staticmethod
    def create_view(auth_type):
        if auth_type == 'signup':
            return SignUpView.as_view()
        elif auth_type == 'signin':
            return SignInView.as_view()
        elif auth_type == 'logout':
            return LogoutView.as_view()
        else:
            raise ValueError(f"Unsupported authentication type: {auth_type}")

class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return redirect('home')
            # Implement your user registration logic here
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignInView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        authenticate_user = authenticate(username = username, password = password)
        if authenticate_user is None:
            return render(request,'signin.html')
        login(request, authenticate_user)
        return redirect('home')


class LogoutView(APIView):
    def post(self, request):
        login(request)
        return render(request,'signin.html')


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


