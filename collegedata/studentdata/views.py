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
             
    if request.method == 'POST':
        print("$$$$$Inside DepartmentApi POSTRequest")
        try:
            # department_data = JSONParser().parse(request)
            print("request_____data",request.data)
            department_serializer = DepartmentsSerializer(data=request.data)
            print("department_serializer",department_serializer)
            if department_serializer.is_valid():
                department_serializer.save()
                print("reached")
                return Response(department_serializer.data,status = status.HTTP_201_CREATED)
            return Response("Failed to Add the POST Request", safe=False)
        except Exception as e:
            print("error---------")
            df = {
                "Error_Message" : "Something went wrong in DepartmentAPI POST METHOD",
                "Error" : e
            }
            
            return df
      