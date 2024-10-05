from .models import CustomUser 
from django import forms 

class CustomUserForm(forms.Form):
    username = forms.CharField(max_length=200, min_length=1, strip=True, empty_value=None, required=True)
    password = forms.CharField(max_length=200, min_length=1, widget=forms.PasswordInput())

