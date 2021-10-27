from typing import Text
from django import forms
from django.forms import ModelForm
from django.db.models.enums import Choices
from django.contrib.auth.models import User
from .models import *
from .views import *


class SignUpForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Full Name",
            "class": "form-control"
        }))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Username",
            "class": "form-control"
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Email",
        "class": "form-control"
    }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password",
            "class": "form-control"
        }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Re-Enter Password",
            "class": "form-control"
        }))

    class Meta:
        model = Customer
        fields = ("full_name", "email", "username", "password",
                  "confirm_password", "department")

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Username already exists. Please choose another username.")
        return uname

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")
        return cleaned_data


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Username",
            "class": "form-control"
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password",
            "class": "form-control"
        }))


class Module1Form(forms.ModelForm):
    class Meta:
        model = Module1
        fields = ("word1", "word2", "question", "right_option",
                  "first_wrong_option", "second_wrong_option",
                  "third_wrong_option")


class Module2Form(forms.ModelForm):
    class Meta:
        model = Module2
        fields = ("word1", "word2", "question", "right_option",
                  "first_wrong_option", "second_wrong_option",
                  "third_wrong_option")


class Module3Form(forms.ModelForm):
    class Meta:
        model = Module3
        fields = ("word1", "word2", "question", "right_option",
                  "first_wrong_option", "second_wrong_option",
                  "third_wrong_option")
