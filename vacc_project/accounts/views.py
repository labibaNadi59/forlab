from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import ParentForm, HospitalForm, ParentProfileForm
from .models import Parent, Hospital
from vaccination.models import Child

from appointments.models import Appointment
# Create your views here.
def home(request):
    return render(request, 'home.html')


def register_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.role = 'parent'
            user.save()
            Parent.objects.create(user = user)
            login(request, user)
            return redirect('parent_dashboard')
    else:
        form = ParentForm()
    return render(request, 'register_parent.html',{'form':form})

def register_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.role = 'hospital'
            user.save()
            Hospital.objects.create(user = user)
            login(request, user)
            return redirect('hospital_dashboard')
    else:
        form = HospitalForm()
    return render(request, 'register_hospital.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'hospital':
                return redirect('hospital_dashboard')
            else:
                return redirect('parent_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def hospital_dashboard(request):
    return render(request, 'hospital_dashboard.html')

def parent_dashboard(request):
    parent = Parent.objects.get(user=request.user)
    children = Child.objects.filter(parent=parent)
    appointments = Appointment.objects.filter(parent=parent)
    completed = appointments.filter(status='completed').count()
    pending = appointments.filter(status='pending').count()
    return render(request, 'parent_dashboard.html', {
        'children': children,
        'appointments': appointments,
        'completed': completed,
        'pending': pending,
        'parent': parent,
    })
def parent_profile(request):
    parent = Parent.objects.get(user=request.user)
    if request.method == 'POST':
        form = ParentProfileForm(request.POST, request.FILES, instance=parent)
        if form.is_valid():
            form.save()
            return redirect('parent_dashboard')
    else:
        form = ParentProfileForm(instance=parent)
    return render(request, 'parent_profile.html', {'form': form, 'parent': parent})


def parent_photo_delete(request):
    parent = Parent.objects.get(user=request.user)
    if request.method == 'POST':
        parent.photo.delete()
        parent.photo = None
        parent.save()
        return redirect('parent_profile')