import json
from urllib.request import urlopen, Request
import requests
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from .models import EmployeeModel
from .serializer import EmployeeSerializer
from rest_framework.response import Response

# Create your views here.

def fetch_employees():
    api_url = 'http://dummy.restapiexample.com/api/v1/employees'
    req = Request(api_url,headers={'User-Agent': 'Mozilla/5.0'})
    res = urlopen(req).read()
    data_json = json.loads(res)
    data = data_json['data']
    return data

class EmployeeList(APIView):
    
    def get(request,*args,**kwargs):
        # Fetch Employee data to 3rd Party API
        data = fetch_employees()

        # Save Data TO DATABASE
        for record in data:
            EmployeeModel.objects.create(emp_id=record['id'],emp_name=record['employee_name'],emp_salary=record['employee_salary'],emp_age=record['employee_age'])
        
        # Fetch All Employee Records From DATABASE
        employees = EmployeeModel.objects.all()

        # Pass Data To Serializer
        employee_serializer = EmployeeSerializer(employees, many=True, context={'request': request})
        return Response({
            'data':{
                'employee_list':employee_serializer.data
            },
            'success': 1
        })