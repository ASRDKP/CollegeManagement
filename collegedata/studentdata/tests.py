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
            
            
            
            
            
            
            
            
            