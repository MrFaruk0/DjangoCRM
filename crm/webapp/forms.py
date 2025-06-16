from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Client

#Register
class CreateUserForm(UserCreationForm):

    class Meta:
        model=User
        fields = ['username', 'password1', 'password2']

#Login

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Client Form

class CreateClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['firstName', 'lastName', 'email', 'phone', 'address', 'city', 'province', 'country']

#Update Client Form
class UpdateClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['firstName', 'lastName', 'email', 'phone', 'address', 'city', 'province', 'country']

