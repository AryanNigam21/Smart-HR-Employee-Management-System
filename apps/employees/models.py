from django.conf import settings
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    def __str__(self): return self.name

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="employee_profile")
    employee_code = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="employees")
    job_title = models.CharField(max_length=100)
    joining_date = models.DateField()
    phone = models.CharField(max_length=20, blank=True)
    employment_status = models.CharField(max_length=20, default="ACTIVE")
    def __str__(self): return f"{self.employee_code} - {self.user.get_full_name()}"
