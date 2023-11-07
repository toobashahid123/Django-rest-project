from django.contrib import admin
from .models import Company, Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)


class employeeAdmin(admin.ModelAdmin):
    list_display=('name','email','address','company',)
    list_filter=('company',)

admin.site.register(Company,CompanyAdmin)

admin.site.register(Employee,employeeAdmin)
