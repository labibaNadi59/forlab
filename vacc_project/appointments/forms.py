from django import forms
from .models import Appointment, Rating, Reminder
from vaccination.models import Child, Vaccine
from accounts.models import Hospital


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['child', 'hospital', 'vaccine', 'appointment_date']


class RatingForm(forms.ModelForm):
    score = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ['score', 'review']


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['reminder_date', 'message']
