from django.db import models
    


class Company(models.Model):
    company_id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=50, choices=(('IT','IT'),
                                                    ('Non-IT','Non-IT')
                                                    ))
    date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name




class Employee(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(('manager','manager'),
                                                        ('Teacher','Teacher'),
                                                        ('Developer','Developer')
                                                        ))
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    company = models.ForeignKey(Company,  related_name='employees', on_delete=models.CASCADE)
