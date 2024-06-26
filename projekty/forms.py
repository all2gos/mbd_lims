from django import forms
from .models import *

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = '__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'sex': forms.RadioSelect(choices=Patient.SEX_CHOICES),
        }

class EntryForm(forms.Form):
    text = forms.CharField(max_length=200)