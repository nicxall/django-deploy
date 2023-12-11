from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from .forms import Formtask
from django.contrib.auth.forms import AuthenticationForm
from .models import task
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.forms import ModelForm
from django.utils import timezone

# Create your views here.


def UserLogin(request):
	if request.method == 'POST':
		try:
			validation_data = authenticate(
				username = request.POST['username'], password = request.POST['password']

			)
			if validation_data is None:
				return render(request,'signin.html')
			login(request, validation_data)
			return redirect('home')
		except User.DoesNotExist:
			return HttpResponse('Tus datos no se encuentran en la base de datos')
	else:
		return render(request,'signin.html')


def signup(request):
	if request.method != 'POST':
		return render(request,'signup.html')
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				registro = User.objects.create_user(
					request.POST['username'], password = request.POST['password1']

				)
				login(request,registro)
				return redirect('home')
			except IntegrityError:
				return redirect('signup')
		
		return render(request,'signup.html')
@login_required
def UserCloseSession(request):
	logout(request)
	return redirect('signin')
@login_required
def home(request):
	context = request.user.username
	return render(request,'home.html',{'username': context})


@login_required
def TaskCreate(request):
	requestform = Formtask(request.POST)
	if request.method == 'POST' and requestform.is_valid():
		try:
			form_valid = requestform.save(commit=False)
			form_valid.user = request.user
			form_valid.save()
			return redirect('home')
		except asyncio.CancelledError:
			return HttpResponse('La tarea no se pudo crear debido a un error, Vuelve a intentarlo')
	else:
		return render(request,'taskcreate.html')
@login_required
def Tasklist(request):
	filtrar_task = task.objects.filter(user = request.user).order_by('-created','title')
	getdata = task.objects.filter(date_completed__isnull = True, user = request.user)
	count = getdata.count()
	return render(request,'tasklist.html',{'filtrar': filtrar_task,'count': count})
@login_required
def taskdetail(request,pk):
	if request.method == 'POST':
		tasks = get_object_or_404(task, pk=pk)
		form = Formtask(request.POST,instance=tasks)
		form.save()
		return redirect('home')
	else:
		form = task.objects.get(pk=pk)
		
		return render(request,'taskdetail.html',{'form': form})
@login_required
def DeleteTask(request,id):
	deletetask = task.objects.get(id=id)
	deletetask.delete()
	return render(request,'tasklist.html',{'context': deletetask})
@login_required
def completetask(request,pk):
	tasks = get_object_or_404(task, pk = pk, user = request.user)
	tasks.date_completed = timezone.now()
	tasks.save()
	return redirect('home')
	
