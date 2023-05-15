from django.contrib import admin
from .models import CustomUser, Department, Company


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'department', 'first_name', 'last_name')


admin.site.register(CustomUser, CustomUserAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    display = ('name')


admin.site.register(Department, DepartmentAdmin)

class CompanyAdmin(admin.ModelAdmin):
    display = ('name')


admin.site.register(Company, CompanyAdmin)