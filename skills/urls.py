from django.urls import path
from . import views

urlpatterns = [
    path('skills/', views.show_skills, name='skills'),
    path('create/', views.users_create, name='create'),
    path('edit/', views.users_edit, name='edit'),
    path('delete/', views.users_delete, name='delete'),
    path('chart/', views.chart_view, name='chart')
]
