from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginFormUser(AuthenticationForm):
    class Meta:
        # model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Usuario',
            'password': 'Contraseña'
        }

class RegistrationFormUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        labels = {
            'username': 'Usuario',
            'password1': 'Contraseña',
            'password2': 'Repetir contraseña',
            'email': 'Email'
        }