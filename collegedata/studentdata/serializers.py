from rest_framework import serializers
from .models import Departments, StudentDetails, Faculties


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['DepartmentId', 'DepartmentName']



class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ['RollNo','StudentName','Department','Year','Batch','DOB']



class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = ['FacultieId','FacultieName','Department','Salary','DateOfJoining']
        
        
    
    

        
        
    