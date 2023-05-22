from django.contrib import admin
from django.urls import path, include
from HRManagementSystemApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hrfront', views.hr_front),
    path('home', views.index, name='home'),
    path('account', views.create_user),
    path('inbox', views.inbox, name='inbox'),
    path('logout/', views.logout_view, name='logout'),
    path("login", views.login_request, name="login"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
