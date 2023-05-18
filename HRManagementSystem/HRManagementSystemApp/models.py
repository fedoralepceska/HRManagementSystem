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


class Department(models.Model):
    name = models.CharField(max_length=30, choices=DepartmentsChoices.choices)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, default=None)
    date_employment = models.DateField(default='2020-12-12', blank=True)
    usedVacDays = models.IntegerField(default=0, blank=True)
    usedSickLeave = models.IntegerField(default=0, blank=True)
    usedFreeDays = models.IntegerField(default=0, blank=True)
    mobile_phone = models.CharField(default=0, blank=True, max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, default=None)

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)


class Request(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
