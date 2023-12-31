from django.urls import path
from .views import UserSession

urlpatterns = [
    path('', UserSession.as_view(), name = 'signinapi'),

]
