from django.db import models

# Create your models here.
class Employes(models.Model):
   name=models.CharField(max_length=40)
   adres=models.CharField(max_length=100)
   age=models.IntegerField
   
class users(models.Model):
   login=models.CharField(max_length=25)
   password=models.CharField(max_length=10)
   mail=models.CharField(max_length=30)
   telephone_number=models.CharField(max_length=12)
   
class personal_inf(models.Model):
   adres=models.CharField(max_length=100)
   room_number=models.IntegerField(max_length=3)
   team=models.CharField(max_length=2)
   name=models.CharField(max_length=40)
   surname=models.CharField(max_length=40)
   
class laboratories(models.Model):
   lab_name=models.CharField(max_length=40)
   adres=models.CharField(max_length=100)
   web_adres=models.CharField(max_length=40)
   mail=models.CharField(max_length=30)
   
class projects(models.Model):
   project_name=models.CharField(max_length=30)
   team_leader=models.CharField(max_length=40)
   description=models.CharField(max_length=40)
   
class experiments (models.Model):
   worker=models.CharField(max_length=50)
   experiment_name=models.CharField(max_length=50)
   description=models.CharField(max_length = 50)
   method=models.CharField(max_length=50)
   
class metody (models.Model):
   name=models.CharField(max_length=40)
   description=models.CharField(max_length=40)
   
class key_words (models.Model):
   name=models.CharField(max_length=40)
   
class patients (models.Model):
   name=models.CharField(max_length=40)
   surname=models.CharField(max_length=40)
   PESEL=models.CharField(max_length=11)
   birth_name=models.CharField(max_length=40)
   adres=models.CharField(max_length=100)
   mail=models.CharField(max_length=30)
   patientscol=models.CharField(max_length=40)
   status=models.CharField(max_length=20)
   diagnosis=models.CharField(max_length=40)
   sex=models.CharField(max_length=10)
   
class diagnosis(models.Model):
   icd_10=models.CharField(max_length=5)