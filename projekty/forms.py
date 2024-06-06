from django import forms
from .models import projects

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = projects
        fields = ['project_name','team_leader','description']