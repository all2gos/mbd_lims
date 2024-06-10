from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages  
from .models import *
from .forms import *
# Create your views here.

def welcome(request):
    return render(request, 'home.html')

@login_required
def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project': project})

@login_required
def employes_home(request):
	l = Employee.objects.all()
	
	return render(request, 'employes.html',{'l':l})

@login_required
def projects_home(request):
	c = Project.objects.count()
	l = Project.objects.all()
	
	return render(request, 'projects_home.html',{'c':c, 'l':l})

def add_project(request):
	return render(request, 'add_project.html')

def add_medical_test(request):
	return render(request, 'add_medical_test.html')

@login_required
def home_user(request):
	return render(request, 'home_user.html')

@login_required
def submit_project(request):
	form = ProjectsForm(request.POST)

	if form.is_valid():
		form.save()
		return redirect('projects')
	else:
		form = ProjectsForm()
	return render(request, 'submit_project.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home_user')  
            else:
                messages.error(request, 'Nieprawidłowe dane logowania. Spróbuj ponownie.')  # Dodaj komunikat
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/home')  # przekierowanie na stronę domową po wylogowaniu

