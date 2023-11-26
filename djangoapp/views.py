from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee
from .serializer import companyserializer, employeeserializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):    
    queryset = Company.objects.all()
    serializer_class = companyserializer


    @action (detail=True, methods=['get'])
    def employees(self,request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = employeeserializer(emps, many=True,context={'request': request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'Company might not exist! ERROR'})
        



class employeeViewSet(viewsets.ModelViewSet):    
    queryset = Employee.objects.all()
    serializer_class = employeeserializer

    def retrieve(self, request, pk=None):
        Company = Company.objects.get(id=pk)
        employee = Company.employees.all()
        paginator = PageNumberPagination()
        paginator.page_size = 20
        queryset=paginator.paginate_queryset(employee, request)
        serializer = self.serializer_class(queryset,many=True)
        return paginator.get_paginated_response(serializer.data)



        

