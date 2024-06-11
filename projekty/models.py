from django.db import models

# Create your models here.

class Project(models.Model):
   project_name=models.CharField(max_length=30)
   team_leader=models.CharField(max_length=30)
   description=models.CharField(max_length=400, null=True)

   class Meta:
      permissions = [
      ('view_projects', 'Can view projects'),
      ('add_projects', 'Can add projects'),
      ('change_projects', 'Can change projects'),
        ]

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

#pojedyncze badanie medyczne
class Experiment(models.Model):
   worker= models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
   patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
   experiment_name=models.CharField(max_length=50, null=True)
   description=models.CharField(max_length = 500, null=True)
   method=models.ForeignKey(Method, on_delete=models.SET_NULL, null=True)

   class Meta:
      permissions = [
         ('view_experiments', 'Can view experiments'),
         ('add_experiments', 'Can add experiments'),
         ('change_experiments', 'Can change experiments'),
      ]

class Laboratory(models.Model):
   lab_name=models.CharField(max_length=40)
   adres=models.CharField(max_length=100)
   web_adres=models.CharField(max_length=40)
   mail=models.CharField(max_length=30)
   
class KeyWord(models.Model):
   name=models.CharField(max_length=40)
     
class Diagnosis(models.Model):
   icd_10=models.CharField(max_length=5)