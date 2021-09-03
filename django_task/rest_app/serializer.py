from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    emp_id = serializers.IntegerField()
    emp_name = serializers.CharField()
    emp_salary = serializers.IntegerField()
    emp_age = serializers.IntegerField()