from rest_framework import serializers
from .models import Company, Employee

class companyserializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"