from django.db import models

# Create your models here.

class Project(models.Model):
   project_name=models.CharField(max_length=30)
   team_leader=models.CharField(max_length=30)
   description=models.CharField(max_length=400)

class Employee(models.Model):
   full_name=models.CharField(max_length=40)
   mail=models.CharField(max_length=40, null=True)
   position=models.CharField(max_length=100)
   adres=models.CharField(max_length=100)
   room_number=models.IntegerField()
   telephone_number=models.CharField(max_length=12, null=True)
   team = models.ManyToManyField(Project)

class Patient(models.Model):
   full_name=models.CharField(max_length=40)
   PESEL=models.CharField(max_length=11)
   birth_name=models.CharField(max_length=40)
   adres=models.CharField(max_length=100)
   mail=models.CharField(max_length=30)
   status=models.CharField(max_length=20)
   diagnosis=models.CharField(max_length=40)
   sex=models.CharField(max_length=10)

class Method(models.Model):
   name=models.CharField(max_length=40)
   description=models.CharField(max_length=40)

class Experiments (models.Model):
   worker= models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
   patients = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
   experiment_name=models.CharField(max_length=50)
   description=models.CharField(max_length = 50)
   method=models.ForeignKey(Method, on_delete=models.SET_NULL, null=True)

class Laboratory(models.Model):
   lab_name=models.CharField(max_length=40)
   adres=models.CharField(max_length=100)
   web_adres=models.CharField(max_length=40)
   mail=models.CharField(max_length=30)
   
class KeyWord(models.Model):
   name=models.CharField(max_length=40)
     
class Diagnosis(models.Model):
   icd_10=models.CharField(max_length=5)