"""
URL configuration for vacc_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/parent/', views.register_parent, name='register_parent'),
    path('register/hospital/', views.register_hospital, name='register_hospital'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/hospital/', views.hospital_dashboard, name='hospital_dashboard'),
    path('dashboard/parent/', views.parent_dashboard, name='parent_dashboard'),
    path('profile/parent/', views.parent_profile, name='parent_profile'),
    path('profile/parent/photo/delete/', views.parent_photo_delete, name='parent_photo_delete'),
    path('profile/admin/', views.admin_profile, name='admin_profile'),
    path('profile/admin/photo/delete/', views.admin_photo_delete, name='admin_photo_delete'),
    path('profile/hospital/', views.hospital_profile, name='hospital_profile'),
    path('profile/hospital/logo/delete/', views.hospital_logo_delete, name='hospital_logo_delete'),
path('manage/parents/', views.manage_parents, name='manage_parents'),
path('manage/parents/delete/<int:parent_id>/', views.delete_parent, name='delete_parent'),
path('manage/hospitals/', views.manage_hospitals, name='manage_hospitals'),
path('manage/hospitals/delete/<int:hospital_id>/', views.delete_hospital, name='delete_hospital'),
path('manage/appointments/', views.manage_appointments, name='manage_appointments'),


]
