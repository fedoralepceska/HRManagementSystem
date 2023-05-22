from django.contrib import admin
from django.urls import path, include
from HRManagementSystemApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hrfront', views.hr_front),
    path('home', views.index, name='home'),
    path('account', views.create_user),
    path('inbox', views.inbox),
    path('logout/', views.logout_view, name='logout'),
]
