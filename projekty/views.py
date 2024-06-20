from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages  
from django.contrib.auth.decorators import user_passes_test

from .models import *
from .forms import *

def check_is_kierownik(user):
    return user.groups.filter(name__in=['Admin', 'Kierownik']).exists()

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
def badania(request):
	l = Experiment.objects.all()
	
	return render(request, 'badania.html',{'l':l})

@login_required
def projects_home(request):
	c = Project.objects.count()
	l = Project.objects.all()
	
	return render(request, 'projects_home.html',{'c':c, 'l':l})

@user_passes_test(check_is_kierownik,login_url='/home_user/')
def add_project(request):
    team_leaders = Employee.objects.all()
    return render(request, 'add_project.html',{'team_leaders': team_leaders})

@login_required
def add_medical_test(request):
    workers = Employee.objects.all()
    patients = Patient.objects.all()
    methods = Method.objects.all()
    return render(request, 'add_medical_test.html', {'workers':workers, 'patients':patients, 'methods':methods})

@login_required
def add_patient(request):
     return render(request, 'add_patient.html')

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
	return render(request, 'submit.html', {'form':form})

@login_required
def submit_medical_test(request):
    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('badania')
    else:
        form = ExperimentForm()
        
    return render(request, 'submit.html', {'form': form})

@login_required
def submit_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_user')
    else:
        form = PatientForm()
        
    return render(request, 'submit.html', {'form': form})

def about_us(request):
      return render(request, 'about_us.html')

def info(request):
     return render(request, 'project_description.html')
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

def checking(request):
     return render(request, 'checking.html')

def search_entries(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            entries = Experiment.objects.filter(experiment_name__exact=text)
            return render(request, 'search_result.html', {'entries': entries})
    else:
        form = EntryForm()
    return render(request, 'search_entries.html', {'form': form})


def search_result(request):
    return render(request, 'search_result.html')