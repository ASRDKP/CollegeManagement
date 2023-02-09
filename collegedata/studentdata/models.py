from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)
    
class StudentDetails(models.Model):
    RollNo = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=500)
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    Year = models.IntegerField(null=True)
    Batch = models.IntegerField(null=True)
    DOB = models.DateField(null=True)
    
class Faculties(models.Model):
    FacultieId  = models.AutoField(primary_key=True)
    FacultieName = models.CharField(max_length=500) 
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    Salary = models.IntegerField(null=True)
    DateOfJoining = models.DateField(null=True)

    
    