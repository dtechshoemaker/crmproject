from django import forms
from .models import Lead
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'John',
        'class': 'inputclass'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Joe',
        'class': 'inputclass'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your alias',
        'class': 'inputclass'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'something@example.com',
        'class': 'inputclass'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'inputclass'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'inputclass'
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your alias',
        'class': 'inputclass'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'inputclass'
    }))



class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'



    