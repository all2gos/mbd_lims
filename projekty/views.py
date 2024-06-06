from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages  
from .models import *
from .forms import *
# Create your views here.

def welcome(request):
    return render(request, 'home.html')
	
def project_detail(request, project_id):
    project = projects.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project': project})
	
def project_home(request):
	c = projects.objects.count()
	l = projects.objects.all()
	
	return render(request, 'project_home.html',{'c':c, 'l':l})

def overall(request):
	return render(request, 'add_project.html')

def overall2(request):
	return render(request, 'home_user.html')

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

