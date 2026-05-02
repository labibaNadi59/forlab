from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import ParentForm, HospitalForm, ParentProfileForm, AdminProfileForm, HospitalProfileForm
from .models import Parent, Hospital
from vaccination.models import Child

from appointments.models import Appointment, Reminder




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
    return render(request, 'admin_dashboard.html', {
        'user': request.user
    })


def hospital_dashboard(request):
    hospital = Hospital.objects.get(user=request.user)
    appointments = Appointment.objects.filter(hospital=hospital)
    completed = appointments.filter(status='completed').count()
    pending = appointments.filter(status='pending').count()
    return render(request, 'hospital_dashboard.html', {
        'hospital': hospital,
        'appointments': appointments,
        'completed': completed,
        'pending': pending,
    })


def parent_dashboard(request):
    parent = Parent.objects.get(user=request.user)
    children = Child.objects.filter(parent=parent)
    appointments = Appointment.objects.filter(parent=parent)
    completed = appointments.filter(status='completed').count()
    pending = appointments.filter(status='pending').count()

    reminders = Reminder.objects.filter(appointment__parent=parent)

    return render(request, 'parent_dashboard.html', {
        'children': children,
        'appointments': appointments,
        'completed': completed,
        'pending': pending,
        'parent': parent,
        'reminders': reminders,
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

def admin_profile(request):
    if request.method == 'POST':
        form = AdminProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = AdminProfileForm(instance=request.user)
    return render(request, 'admin_profile.html', {'form': form})


def admin_photo_delete(request):
    if request.method == 'POST':
        request.user.photo.delete()
        request.user.photo = None
        request.user.save()
        return redirect('admin_profile')

def hospital_profile(request):
    hospital = Hospital.objects.get(user=request.user)
    if request.method == 'POST':
        form = HospitalProfileForm(request.POST, request.FILES, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_dashboard')
    else:
        form = HospitalProfileForm(instance=hospital)
    return render(request, 'hospital_profile.html', {'form': form, 'hospital': hospital})


def hospital_logo_delete(request):
    hospital = Hospital.objects.get(user=request.user)
    if request.method == 'POST':
        hospital.logo.delete()
        hospital.logo = None
        hospital.save()
        return redirect('hospital_profile')
