from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def welcome(request):
	message = 'Formularz logowania, wprowadzania eksperymentu, pojedycznych badań etc.'
	return HttpResponse(message)
	

def project_detail(request, project_id):
    project = projects.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project': project})
	

def db_pretty(request):
	c = projects.objects.count()
	l = projects.objects.all()
	
	return render(request, 'base_temp.html',{'c':c, 'l':l})

def overall(request):

	return render(request, 'add_project.html')


def submit_project(request):
	form = ProjectsForm(request.POST)

	if form.is_valid():
		form.save()
		return redirect('projects')
	else:
		form = ProjectsForm()
	return render(request, 'submit_project.html', {'form':form})