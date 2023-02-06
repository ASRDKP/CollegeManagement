from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^department$', views.departmentApi),
    re_path(r'department/(?P<id>\d+)',views.departmentApi),
    
    re_path(r'^studentDetails$', views.studentDetailsApi),
    re_path(r'studentDetails/(?P<id>\d+)',views.studentDetailsApi)
]
