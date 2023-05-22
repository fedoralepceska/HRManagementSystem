from django.contrib import admin
from django.urls import path, include
from HRManagementSystemApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hrfront', views.hr_front, name='hrfront'),
    path('home', views.index, name='home'),
    path('account', views.create_user),
    path('inbox-hr', views.inbox_hr, name='inbox-hr'),
    path('inbox-user', views.inbox_user, name='inbox-user'),
    path('logout/', views.logout_view, name='logout'),
    path("login", views.login_request, name="login"),
    path("request-user", views.request_user, name="request-user"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
