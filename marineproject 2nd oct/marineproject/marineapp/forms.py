from typing import Text
from django import forms
from django.db.models.enums import Choices
from .models import User

from django.contrib.auth.models import User

from .views import *


class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = Customer
        fields = ("full_name", "email", "username", "password", "email",
                  "department", "role")

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Username already exists. Please choose another username.")
        return uname


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())