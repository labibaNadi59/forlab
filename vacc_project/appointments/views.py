from django.shortcuts import render, redirect
from .models import Appointment, Rating, Reminder
from .forms import AppointmentForm, RatingForm, ReminderForm
from accounts.models import Parent, Hospital
from vaccination.models import Child


# Create your views here.




#Appointment CRUD operations for Parent

def appointment_list(request):
    parent = Parent.objects.get(user=request.user)
    appointments = Appointment.objects.filter(parent=parent)
    return render(request, 'appointment_list.html', {'appointments': appointments})



def appointment_create(request):
    parent = Parent.objects.get(user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.parent = parent
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
        # show only this parent's children in dropdown
        form.fields['child'].queryset = Child.objects.filter(parent=parent)
    return render(request, 'appointment_form.html', {'form': form})




def appointment_cancel(request, app_id):
    appointment = Appointment.objects.get(pk=app_id)
    appointment.status = 'cancelled'
    appointment.save()
    return redirect('appointment_list')


def appointment_reschedule(request, app_id):
    appointment = Appointment.objects.get(pk=app_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
        parent = Parent.objects.get(user=request.user)
        form.fields['child'].queryset = Child.objects.filter(parent=parent)
    return render(request, 'appointment_form.html', {'form': form})

#Appointment Management system for Hospital



def hospital_appointments(request):
    hospital = Hospital.objects.get(user=request.user)
    appointments = Appointment.objects.filter(hospital=hospital)
    return render(request, 'hospital_appointments.html', {'appointments': appointments})


def appointment_accept(request, app_id):
    appointment = Appointment.objects.get(pk=app_id)
    appointment.status = 'accepted'
    appointment.save()
    return redirect('hospital_appointments')



def appointment_complete(request, app_id):
    appointment = Appointment.objects.get(pk=app_id)
    appointment.status = 'completed'
    appointment.save()
    return redirect('hospital_appointments')


def appointment_missed(request, app_id):
    appointment = Appointment.objects.get(pk=app_id)
    appointment.status = 'missed'
    appointment.save()
    return redirect('hospital_appointments')





#Rating system for Parent



def rate_hospital(request, rate_id):
    appointment = Appointment.objects.get(pk=rate_id)
    parent = Parent.objects.get(user=request.user)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.parent = parent
            rating.hospital = appointment.hospital
            rating.appointment = appointment
            rating.save()
            return redirect('appointment_list')
    else:
        form = RatingForm()
    return render(request, 'rating_form.html', {'form': form})

#---- arnob
def set_reminder(request, app_id):
    appointment = Appointment.objects.get(pk=app_id)
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.appointment = appointment
            reminder.save()
            return redirect('parent_dashboard')
    else:
        form = ReminderForm()
    return render(request, 'reminder_form.html', {'form': form, 'appointment': appointment})


def delete_reminder(request, app_id):
    appointment = Appointment.objects.get(pk=app_id)
    if request.method == 'POST':
        appointment.reminder.delete()
        return redirect('parent_dashboard')

