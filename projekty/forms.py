from django import forms
from .models import Project

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name','team_leader','description']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

