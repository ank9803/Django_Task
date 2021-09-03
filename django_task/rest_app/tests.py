import json
import names
from rest_framework import status
from rest_framework.test import APITestCase, HeaderDict
from django.test import TestCase
from rest_app.models import EmployeeModel

# Create your tests here.

import random

def random_num(a,b):
    n = random.randint(a,b)
    return n

class EmployeeTestCase(APITestCase):
    
    def test_employee(self):
        data = {
            'emp_id':random_num(0,999),
            'emp_name':names.get_full_name(),
            'emp_salary':random_num(5000,50000),
            'emp_age':random_num(0,100)
        }

        response = self.client.get("/employee/get/",data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

