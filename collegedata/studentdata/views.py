from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from studentdata.models import Departments, StudentDetails, Faculties
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view
from studentdata.serializers import DepartmentsSerializer, StudentDetailsSerializer, FacultiesSerializer
from rest_framework.parsers import JSONParser
# Create your views here.

@csrf_exempt
@api_view(['GET','POST','DELETE','PUT'])
def departmentApi(request, id=None):
    if request.method == 'GET' and id == None:
        try:
            print("Inside GET method without id parameter")
            departments_data = Departments.objects.all() 
            department_serializer = DepartmentsSerializer(departments_data,many=True)
            return JsonResponse(department_serializer.data,safe=False)
        except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in DepartmentAPI GET METHOD",
                "Error" : e
            }       
            return df
        

             
    if request.method == 'POST':
        try:
            department_serializer = DepartmentsSerializer(data=request.data)
            if department_serializer.is_valid():
                department_serializer.save()
                return Response(department_serializer.data,status = status.HTTP_201_CREATED)
            return Response("Failed to Add the POST Request", safe=False)
        except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in DepartmentAPI POST METHOD",
                "Error" : e
            }
            
            return df
    
    
    if request.method == 'DELETE':
        try:
            department_data = Departments.objects.get(pk=id)
            department_data.delete()
            return redirect('/department')
        except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in DepartmentAPI DELETE METHOD",
                "Error" : e
            }
            
            return df        






@csrf_exempt
@api_view(['GET','POST','DELETE'])
def studentDetailsApi(request, id=0):
    if request.method == 'GET' and id == 0:
        try:
            studentDetails_data = StudentDetails.objects.all() 
            studentDetails_serializer = StudentDetailsSerializer(studentDetails_data,many=True)
            return JsonResponse(studentDetails_serializer.data,safe=False)
        except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in studentDetailsApi GET METHOD",
                "Error" : e
            }       
            return df
        
    
        
        
    if request.method == 'POST':
        try:
            studentDetails_serializer = StudentDetailsSerializer(data = request.data)
            if studentDetails_serializer.is_valid():
                studentDetails_serializer.save()
                return Response(studentDetails_serializer.data, status = status.HTTP_201_CREATED)
            return Response("Failed to Add the POST Request", safe=False)
        except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in studentDetailsApi POST METHOD",
                "Error" : e
            }    
            return df
            
    
    if request.method == 'DELETE':
        try:
            studentDetails_data = StudentDetails.objects.get(pk=id) 
            studentDetails_data.delete()
            return redirect('/studentDetails')
        except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in StudentDetailsAPI DELETE METHOD",
                "Error" : e
            }
            
            return df        







@csrf_exempt
@api_view(['GET','POST','DELETE'])
def facultiesApi(request, id=None):
    if request.method == 'GET' and id == None:
        try:
            faculties_data = Faculties.objects.all()
            print("faculties_data : ", faculties_data)
            faculties_serializer = FacultiesSerializer(faculties_data,many=True)
            print("faculties_serializer : ", faculties_serializer)
            return JsonResponse(faculties_serializer.data,safe=False)
        except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in facultiesApi GET METHOD",
                "Error" : e
            }
            return df
        
    if request.method == 'GET' and id != None:
        try:
            faculties_data = Faculties.objects.get(pk=id)
            faculties_serializer = FacultiesSerializer(faculties_data)
            return JsonResponse(faculties_serializer.data,safe=True)
        except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in facultiesApi GET METHOD",
                "Error" : e
            }
            return df       
        
    if request.method == 'POST':
        try:
            faculties_serializer = FacultiesSerializer(data=request.data)
            if faculties_serializer.is_valid():
                faculties_serializer.save()
                return Response(faculties_serializer.data, status = status.HTTP_201_CREATED)
            return Response("Failed to Add the POST Request", safe=False)
        except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in facultiesApi POST METHOD",
                "Error" : e
            }
            return df
        
        
    if request.method == 'DELETE':
        try:
            faculties_data = Faculties.objects.get(FacultieId=id)
            faculties_data.delete()
            return redirect('/faculties')
        except Exception as e:
            df = {
                "Error_Message" : "Something went wrong in facultiesApi DELETE METHOD",
                "Error" : e
            }

            return df
            
            

