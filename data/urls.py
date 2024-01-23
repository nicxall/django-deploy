from django.urls import path
from .views import CreateTask, AuthenticationViewFactory

urlpatterns = [
    path('create/task/', CreateTask.as_view(), name = 'createtaskapi'),
    path('', AuthenticationViewFactory.create_view('signin'), name = 'factorysignin'),
    path('account/signup/', AuthenticationViewFactory.create_view('signup'), name = 'factorysignup'),
    path('account/logout/', AuthenticationViewFactory.create_view('logout'), name = 'factorylogout'),

]
