from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.student_login, name='login'),
    path('register/', views.student_register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.student_logout, name='logout'),
]
