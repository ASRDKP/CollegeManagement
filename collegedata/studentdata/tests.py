import json
import unittest
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from .models import *
from .serializers import *

from faker import Faker
fake = Faker()


print("********************************")
for _ in range(0, 10):
    print(fake.name())



class FirstTestCase(TestCase):

    def test_equals(self):
        self.assertEqual(1,1)
    
    # def test_equals(self):
    #     self.assertEqual(1,2)







# class DepartmentsTest(APITestCase):
    
#     def test_departments(self):
#         print ("Testing Departments")
#         data = {
#             'DepartmentId' : '03',
#             'DepartmentName' : 'CSIT'
#         }
        
#         data1 = json.dumps(data)
        
#         print("_data : ", data)
#         try :
#             _responce = self.client.post('/department/', data1, format = 'json')
#             print("_responce", _responce)
#         except Exception as e:
#             print("Error Message 1: ", e)
        
        
#         # try:
#         #     _data = _responce
#         # except Exception as e:
#         #     print("Error Message : ", e)
            
#         self.assertEquals(_responce.status_code, status.HTTP_201_CREATED)



    
    
    
    
    
### Departments TestCases
    
class test_DepartmentsTest(TestCase):
    
    def setUp(self):
        print("Setup Called")
        
   
   
    def test_departments(self):
        try:
            print("Testing deptnames")
            
            deptnames = ['IT', 'CS', 'EC']
            print("Deptnames", deptnames)
            
            for deptname in deptnames:
                obj = Departments.objects.create(
                    DepartmentName = deptname
                )
                
                self.assertEquals(deptname, obj.DepartmentName)
                print("obj :", obj)
            
            objs = Departments.objects.all()
            
            self.assertEquals(objs.count(), 3)
        
        except Exception as e:
            print("Error in test_departments :", e)
    
    
    
    def test_full_departments(self):
        try:
            print("Testing Full Departments")
            
            dids = ['01','02']
            dNames = ['IT','CS']
            
            for i in range(2):
                obj = Faculties.objects.create(
                    DepartmentId = dids[i],
                    DepartmentName = dNames[i]
                )
                
                self.assertEquals(dids[i], obj.DepartmentId)
                self.assertEquals(dNames[i], obj.DepartmentName)
                
            objs = Departments.objects.all()
            
            self.assertEquals(objs.count(), 2)
            
        except Exception as e:
            print("Error in test_full_departments :", e)
            
            
            
            












### Student Test Cases        
            
class test_StudentDetailsTest(TestCase):
    
    def setUp(self):
        print("Setup Called")
        
   
   
        
    def test_studentDetails(self):
        try:
            print("Testing student details")
            
            sNames = ['Rahul', 'Rohan', 'Ishita', 'Sanjana']
            
            for sName in sNames:
                obj = StudentDetails.objects.create(
                    StudentName = sName
                )
                
                self.assertEquals(sName, obj.StudentName)
                
            objs = StudentDetails.objects.all()
            
            self.assertEquals(objs.count(), 4)
        
        except Exception as e:
            print("Error in test_studentDetails :", e)
            
            
            
    def test_full_StudentDetails(self):
        try:
            print("Testing Full Student Details")
            
            rNos = ['36','12','15']
            sNames = ['Rahul','Ishita', 'Rakesh']
            dNames = ["02","02","01"]
            years = [2016,2016,2016]
            batch = [2019, 2019, 2019]
            dobs = ["2001-07-04","2001-06-01","2001-12-10"]
            
            for i in range(3):
                obj = StudentDetails.objects.create(
                    RollNo = rNos[i],
                    StudentName = sNames[i],
                    Department = dNames[i],
                    Year = years[i],
                    Batch = batch[i],
                    DOB = dobs[i]
                )
                
                self.assertEquals(rNos[i], obj.RollNo)
                self.assertEquals(sNames[i], obj.StudentName)
                self.assertEquals(dNames[i], obj.Department)
                self.assertEquals(years[i], obj.Year)
                self.assertEquals(dobs[i], obj.DOB)
                
            objs = StudentDetails.objects.all()
            
            self.assertEquals(objs.count(), 3)

        except Exception as e:
            print("Error in test_full_StudentDetails :", e) 
            
            






            
            
            




##### Faculties Test Cases

class test_Faculties(TestCase):
    
    def setUp(self):
        print("Setup Called")
        
    def test_faculties(self):
        try:
            print("Testing faculties")
            
            fNames = ['Radheshyam', 'Avijith', 'Amit']
            
            for fName in fNames:
                obj = Faculties.objects.create(
                    FacultieName = fName
                )
                
                self.assertEquals(fName, obj.FacultieName)
                
            objs = Faculties.objects.all()
            
            self.assertEquals(objs.count(), 3)
            
        except Exception as e:
            print("Error in test_faculties :", e)

            

    def test_full_faculties(self):
        try:
            print("Testing Full Faculties")  
            
            fids = [136,120, 11]
            fnames = ['Radheshyam', 'Avijith','Surender']
            dept = ["02","02","01"]
            salaries = [60000, 55000, 20000]
            doj = ["2016-08-15","2016-08-15","2016-08-15"]
            
            for i in range(3):
                obj = Faculties.objects.create(
                    FacultieId = fids[i],
                    FacultieName = fnames[i],
                    Department = dept[i],
                    Salary = salaries[i],
                    DateOfJoining = doj[i]
                )
                
                self.assertEquals(fids[i], obj.FacultieId)
                self.assertEquals(fnames[i], obj.FacultieName)
                self.assertEquals(dept[i], obj.Department)
                self.assertEquals(salaries[i], obj.Salary)
                self.assertEquals(doj[i], obj.DateOfJoining)
                
            objs = Faculties.objects.all()
            
            self.assertEquals(objs.count(), 3)
            
        except Exception as e:
            print("Error in test_full_faculties :", e) 
            
            
