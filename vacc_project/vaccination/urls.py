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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('vaccines/', views.vaccine_list, name='vaccine_list'),
    path('vaccines/add/', views.vaccine_create, name='vaccine_create'),
    path('vaccines/edit/<int:pk>/', views.vaccine_update, name='vaccine_update'),
    path('vaccines/delete/<int:pk>/', views.vaccine_delete, name='vaccine_delete'),

    path('children/', views.child_list, name='child_list'),
    path('children/add/', views.child_create, name='child_create'),
    path('children/edit/<int:pk>/', views.child_update, name='child_update'),
    path('children/delete/<int:pk>/', views.child_delete, name='child_delete'),
]
