from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'password1' ,'password2' , 'email']

        widgets = {
            'username' : forms.TextInput(attrs={'class': 'is-input', 'placeholder': 'enter a new username' }),
            'password1' : forms.TextInput(attrs={'class': 'is-input', 'placeholder': 'enter a password' }),

            'password2' : forms.TextInput(attrs={'class': 'is-input', 'placeholder': 'enter that password again' }),
            'email' : forms.TextInput(attrs={'class': 'is-input', 'placeholder': 'enter your email'}),

        }
