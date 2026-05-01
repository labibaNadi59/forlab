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

class ParentProfileForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['phone', 'address', 'photo']

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['photo']


class HospitalProfileForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'phone', 'address', 'logo']
