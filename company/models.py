from django.db import models

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length = 42)
    age = models.SmallIntegerField()
    department = models.CharField(max_length = 42)
    created_date = models.DateTimeField(auto_now_add = True, null = False, blank = False) 
    modified_date = models.DateTimeField(auto_now = True, null = False, blank = False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length = 42)
    age = models.SmallIntegerField()
    salary = models.IntegerField()
    designation = models.CharField(max_length = 42)
    created_date = models.DateTimeField(auto_now_add = True, null = False, blank = False) 
    modified_date = models.DateTimeField(auto_now = True, null = False, blank = False)
    reporting_manager = models.ForeignKey(Manager, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name