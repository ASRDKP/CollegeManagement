from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from studentdata.models import Departments, StudentDetails, Faculties
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view
from studentdata.serializers import DepartmentsSerializer, StudentDetailsSerializer, FacultiesSerializer

# Create your views here.

@csrf_exempt
@api_view(['GET','POST','DELETE','PUT'])
def departmentApi(request, id=0):
    print("$$$$$Inside DepartmentApi")
    if request.method == 'GET':
        print("$$$$$Inside DepartmentApi GetRequest")
        try:
            departments_data = Departments.objects.all() 
            # print("Department_data :", departments_data)
            department_serializer = DepartmentsSerializer(departments_data,many=True)
            # print("Department_serializer :", department_serializer.data)
            return JsonResponse(department_serializer.data,safe=False)
        except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in DepartmentAPI GET METHOD",
                "Error" : e
            }       
            return df
             
      