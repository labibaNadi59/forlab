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
    path('', views.appointment_list, name='appointment_list'),
    path('book/', views.appointment_create, name='appointment_create'),
    path('cancel/<int:app_id>/', views.appointment_cancel, name='appointment_cancel'),
    path('reschedule/<int:app_id>/', views.appointment_reschedule, name='appointment_reschedule'),
    path('hospital/', views.hospital_appointments, name='hospital_appointments'),
    path('accept/<int:app_id>/', views.appointment_accept, name='appointment_accept'),
    path('complete/<int:app_id>/', views.appointment_complete, name='appointment_complete'),
    path('missed/<int:app_id>/', views.appointment_missed, name='appointment_missed'),
    path('rate/<int:rate_id>/', views.rate_hospital, name='rate_hospital'),
]
