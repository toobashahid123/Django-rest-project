from django.contrib import admin
from django.urls import path, include
from .views import CompanyViewSet, employeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', employeeViewSet)


urlpatterns = [
    path('', include(router.urls))
    
]
