from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class DepartmentsChoices(models.TextChoices):
    HR = "HR"
    IT = "IT"
    MARKETING = "MARKETING"
    FINANCE = "FINANCE"
    SALES = "SALES"
    MANAGEMENT = "MANAGEMENT"


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    date_employment = models.DateField()
    usedVacDays = models.IntegerField()
    usedSickLeave = models.IntegerField()
    usedFreeDays = models.IntegerField()
    mobile_phone = models.CharField(default=0, blank=True, max_length=20)


class Department(models.TextChoices):
    name = models.CharField(max_length=30, choices=DepartmentsChoices.choices)
    employees = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50)
    employees = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.name
