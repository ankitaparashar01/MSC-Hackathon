from typing import Text
from django import forms
from django.db.models.enums import Choices
from .models import User

from django.contrib.auth.models import User

from .views import *

DEPARTMENT_CHOICES = [
    ('HR', 'HR'),
    ('HOD', 'HOD'),
    ('Trainer', 'Trainer'),
]


class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())
    department = forms.MultipleChoiceField(required=False,
                                           widget=forms.CheckboxSelectMultiple,
                                           choices=DEPARTMENT_CHOICES)

    class Meta:
        model = Customer
        fields = ("full_name", "email", "username", "password", "email",
                  "department")

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Username already exists. Please choose another username.")
        return uname


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())