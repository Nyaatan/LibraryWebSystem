from django import forms
from django.core.exceptions import ValidationError
from .models import User, Subscription


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']
        labels = {'name': 'Username', 'password': 'Password'}
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        }


class SignUpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['user_id'].initial = max(User.objects.values_list('user_id', flat=True)) + 1
        self.fields['subscription'].initial = Subscription.objects.get(price='0').subscription_id
        self.fields['borrowings_remaining'].initial = Subscription.objects.get(price='0').borrowing_count

    class Meta:
        model = User
        fields = ['user_id', 'name', 'password', 'email', 'subscription', 'borrowings_remaining']
        labels = {'name': 'Username', 'password': 'Password', 'email': 'E-mail'}
        widgets = {
            'user_id': forms.HiddenInput,
            'password': forms.PasswordInput,
            'email': forms.EmailInput,
            'subscription': forms.HiddenInput,
            'borrowings_remaining': forms.HiddenInput,
        }
