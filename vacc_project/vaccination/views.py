from django.shortcuts import render,  redirect
from .models import Vaccine, Child
from .forms import VaccineForm, ChildForm
from accounts.models import Parent

# Create your views here.

# Vaccine (CRUD operation) for admin only

def vaccine_list(request):
    vaccines = Vaccine.objects.all()
    return render(request, 'vaccine_list.html', {'vaccines': vaccines})


def vaccine_create(request):
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vaccine_list')
    else:
        form = VaccineForm()
    return render(request, 'vaccine_form.html', {'form': form})


def vaccine_update(request, pk):
    vaccine = Vaccine.objects.get(pk=pk)
    if request.method == 'POST':
        form = VaccineForm(request.POST, instance=vaccine)
        if form.is_valid():
            form.save()
            return redirect('vaccine_list')
    else:
        form = VaccineForm(instance=vaccine)
    return render(request, 'vaccine_form.html', {'form': form})


def vaccine_delete(request, pk):
    Vaccine.objects.get(pk=pk).delete()
    return redirect('vaccine_list')

# ----------------end of vaccine crud


# ---------- start child crud, can mange parent only

def child_list(request):
    parent = Parent.objects.get(user=request.user)
    children = Child.objects.filter(parent=parent)
    return render(request, 'child_list.html', {'children': children})


def child_create(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.parent = Parent.objects.get(user=request.user)
            child.save()
            return redirect('child_list')
    else:
        form = ChildForm()
    return render(request, 'child_form.html', {'form': form})


def child_update(request, pk):
    child = Child.objects.get(pk=pk)
    if request.method == 'POST':
        form = ChildForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            return redirect('child_list')
    else:
        form = ChildForm(instance=child)
    return render(request, 'child_form.html', {'form': form})


def child_delete(request, pk):
    Child.objects.get(pk=pk).delete()
    return redirect('child_list')