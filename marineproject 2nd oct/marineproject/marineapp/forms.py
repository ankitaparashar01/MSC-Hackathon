from typing import Text
from django import forms
from django.db.models.enums import Choices
from django.contrib.auth.models import User
from django.forms import ModelForm
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
        fields = (
            "full_name",
            "email",
            "username",
            "password",
            "confirm_password",
            #   "department",
            "hr",
            "trainer",
            "trainee")

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
        if (len(password) < 9):
            self.add_error('password',
                           'Use a password with a minimum of 10 charcters.')
        if password.isdigit():
            self.add_error(
                'password',
                'password must contains both aplhabets and numbers')
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
        fields = ("question", "right_option",
                  "first_wrong_option", "second_wrong_option",
                  "third_wrong_option", "explanation")


class Module2Form(forms.ModelForm):
    class Meta:
        model = Module2
        fields = ("question", "right_option",
                  "first_wrong_option", "second_wrong_option",
                  "third_wrong_option", "explanation")


class Module3Form(forms.ModelForm):
    class Meta:
        model = Module3
        fields = ("question", "right_option",
                  "first_wrong_option", "second_wrong_option",
                  "third_wrong_option", "explanation")


class Module4Form(forms.ModelForm):
    class Meta:
        model = Module4
        fields = ("hangman_word", "question", "right_option",
                  "first_wrong_option", "second_wrong_option",
                  "third_wrong_option", "explanation")


class Module5Form(forms.ModelForm):
    class Meta:
        model = Module5
        fields = ("hangman_word", "question", "right_option",
                  "first_wrong_option", "second_wrong_option",
                  "third_wrong_option", "explanation")


class CheckAnswer(forms.Form):
    your_answer = forms.CharField(label='Answer')

    def clean(self):
        cleaned_data = super(CheckAnswer, self).clean()
        response = cleaned_data.get("your_answer")
        try:
            p = Answer.objects.get(answer__iexact=response)
        except Answer.DoesNotExist:
            raise forms.ValidationError("Wrong Answer.")