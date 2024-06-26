"""
URL configuration for lims project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from projekty.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
	path('home/', welcome, name='welcome'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('projects_home/', projects_home, name='projects'),
    path('submit_project/', submit_project, name='submit_project'),
    path('submit_patient/', submit_patient, name='submit_patient'),
    path('submit_medical_test/', submit_medical_test, name='submit_medical_test'),

    path('home_user/',home_user, name='home_user'),
	path('projekty/', include('projekty.urls')),
    path('employes/',employes_home, name='employes'),
    path('add_medical_test/',add_medical_test, name='add_medical_test'),
    path('about_us', about_us, name='about_us'),
    path('add_project/', add_project, name='add_project'),
    path('badania/',badania, name='badania'),
    path('add_patient/',add_patient, name='add_patient'),
    path('checking/',checking, name='checking'),
    path('info/',info, name='info'),
    path('search_entries/',search_entries, name='search_entries'),
    path('search_result/',search_result, name='search_result'),
    path('modify_result/<int:id>', modify_result, name='modify_result'),
    path('projects/filter/', filter_projects, name='filter_projects'), 


]
