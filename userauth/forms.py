from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomSignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput())
    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password')