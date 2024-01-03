from django.urls import path
from myapp import views
from myapp.views import TaskCreate, home
urlpatterns = [
	path('signup/', views.signup , name='signup'),
	path('accounts/logout/', views.UserCloseSession, name='logout'),
	path('inicio/', home.as_view(), name='home'),
	path('task/create/', TaskCreate.as_view(),name='taskcreate'),
	path('task/list/', views.Tasklist, name = 'tasklist'),
	path('task/detail/<int:pk>/', views.taskdetail, name='taskdetail'),
	path('delete/task/<int:id>', views.DeleteTask, name='deletetask'),
	path('completed/task/<int:pk>', views.completetask, name='complete'),
	path('logout/', views.UserCloseSession, name = 'logout'),
]