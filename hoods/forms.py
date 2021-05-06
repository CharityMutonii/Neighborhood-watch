from django import forms
from .models import Profile, Alert, Business
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class NewAlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        exclude = ['user','hood']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','email']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['neighborhood']
