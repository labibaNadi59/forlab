from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Parent, Hospital

class ParentForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class HospitalForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']