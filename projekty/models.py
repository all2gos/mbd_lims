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

   def __str__(self):
      return f"{self.full_name}"

class Patient(models.Model):
   SEX_CHOICES = [
        ('M', 'Mężczyzna'),
        ('K', 'Kobieta'),
    ]
       
   full_name=models.CharField(max_length=40, null=True)
   PESEL=models.CharField(max_length=11, null=True)
   birth_name=models.CharField(max_length=40, null=True)
   adres=models.CharField(max_length=100, null=True)
   mail=models.CharField(max_length=30, null=True)
   diagnosis=models.CharField(max_length=40, null=True)
   sex=models.CharField(max_length=1, choices=SEX_CHOICES, null=True)

   def __str__(self):
      return f"{self.full_name}"
class Method(models.Model):
   name=models.CharField(max_length=40)
   description=models.CharField(max_length=40)

   def __str__(self):
      return f"{self.name}"

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

class Entry(models.Model):
    text = models.CharField(max_length=200)