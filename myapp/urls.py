from django.urls import path
from myapp import views
urlpatterns = [
	path('', views.UserLogin, name='signin'),
	path('signup/', views.signup , name='signup'),
	path('accounts/logout/', views.UserCloseSession, name='logout'),
	path('inicio/', views.home, name='home'),
	path('task/create/', views.TaskCreate, name='taskcreate'),
	path('task/list/', views.Tasklist, name = 'tasklist'),
	path('task/detail/<int:pk>/', views.taskdetail, name='taskdetail'),
	path('delete/task/<int:id>', views.DeleteTask, name='deletetask'),
	path('completed/task/<int:pk>', views.completetask, name='complete')
]