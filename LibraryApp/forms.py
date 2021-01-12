from django import forms
from django.core.exceptions import ValidationError
from .models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']
        labels = {'name': 'Username', 'password': 'Password'}
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        }

