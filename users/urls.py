from django.urls import path, include
from . import views

urlpatterns = [
    path('registration/', views.registration_request, name="register"),
    path('login/', views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("admin/", views.admin_request, name="admin"),
    path("employee/", views.employee_request, name="employee"),
    path('', include('skills.urls')),
]
