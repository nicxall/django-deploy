from django.urls import path
from .views import UserSession, CreateTask

urlpatterns = [
    path('', UserSession.as_view(), name = 'signinapi'),
    path('create/task/', CreateTask.as_view(), name = 'createtaskapi'),

]
