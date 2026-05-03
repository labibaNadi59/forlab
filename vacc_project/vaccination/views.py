from django.shortcuts import render,  redirect
from .models import Vaccine, Child
from .forms import VaccineForm, ChildForm
from accounts.models import Parent
from datetime import date

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


#arnob


def vaccine_suggestions(request, child_id):
    child = Child.objects.get(pk=child_id)

    # calculate age in months
    today = date.today()
    age_in_months = (today.year - child.date_of_birth.year) * 12 + (today.month - child.date_of_birth.month)

    # static suggestion list based on age
    suggestions = []

    if age_in_months <= 2:
        suggestions = [
            {'vaccine': 'BCG', 'description': 'Protects against Tuberculosis'},
            {'vaccine': 'Hepatitis B', 'description': 'First dose at birth'},
        ]
    elif age_in_months <= 4:
        suggestions = [
            {'vaccine': 'DPT', 'description': 'Protects against Diphtheria, Pertussis, Tetanus'},
            {'vaccine': 'Polio (OPV)', 'description': 'Oral Polio Vaccine first dose'},
            {'vaccine': 'Hepatitis B', 'description': 'Second dose'},
        ]
    elif age_in_months <= 6:
        suggestions = [
            {'vaccine': 'DPT', 'description': 'Second dose'},
            {'vaccine': 'Polio (OPV)', 'description': 'Second dose'},
            {'vaccine': 'Influenza', 'description': 'Protects against seasonal flu'},
        ]
    elif age_in_months <= 12:
        suggestions = [
            {'vaccine': 'DPT', 'description': 'Third dose booster'},
            {'vaccine': 'Polio (OPV)', 'description': 'Third dose'},
            {'vaccine': 'Hepatitis B', 'description': 'Third dose'},
        ]
    elif age_in_months <= 18:
        suggestions = [
            {'vaccine': 'MMR', 'description': 'Protects against Measles, Mumps, Rubella'},
            {'vaccine': 'Varicella', 'description': 'Protects against Chickenpox'},
        ]
    elif age_in_months <= 24:
        suggestions = [
            {'vaccine': 'MMR', 'description': 'Second dose booster'},
            {'vaccine': 'Hepatitis A', 'description': 'Protects against Hepatitis A'},
        ]
    else:
        suggestions = [
            {'vaccine': 'Tdap', 'description': 'Tetanus, Diphtheria booster'},
            {'vaccine': 'HPV', 'description': 'Protects against Human Papillomavirus'},
        ]

    return render(request, 'vaccine_suggestions.html', {
        'child': child,
        'suggestions': suggestions,
        'age_in_months': age_in_months,
    })



def select_child_for_suggestions(request):
    parent = Parent.objects.get(user=request.user)
    children = Child.objects.filter(parent=parent)
    return render(request, 'select_child.html', {'children': children})


