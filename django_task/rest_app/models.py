from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=100)
    emp_salary = models.IntegerField()
    emp_age = models.IntegerField()

    def __str__(self):
        return str(self.emp_name)