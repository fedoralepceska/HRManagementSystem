from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True)

    class Department(models.TextChoices):
        HR = "HR"
        IT = "IT"
        MARKETING = "MARKETING"
        FINANCE = "FINANCE"
        SALES = "SALES"
        MANAGEMENT = "MANAGEMENT"

    department = models.CharField(
        max_length=30,
        choices=Department.choices,
        default=Department.MANAGEMENT, )
    date_employment = models.DateField()
    usedVacDays = models.IntegerField()
    usedSickLeave = models.IntegerField()
    usedFreeDays = models.IntegerField()
    mobile_phone = models.CharField(default=0, blank=True, max_length=20)

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)


class Company(models.Model):
    name = models.CharField(max_length=50)
    employees = models.ManyToManyField(CustomUser)
