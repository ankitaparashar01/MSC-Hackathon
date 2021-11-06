from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.enums import Choices
from django.forms.fields import CharField
from multiselectfield import MultiSelectField
from django.forms import ModelForm

# Create your models here.


class Customer(models.Model):
    # DEPARTMENT_CHOICES = [
    #     ('HR', 'HR'),
    #     ('Trainer', 'Trainer'),
    #     ('Trainee', 'Trainee'),
    # ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField("Full Name", max_length=250)
    email = models.EmailField()
    # department = MultiSelectField(choices=DEPARTMENT_CHOICES)
    hr = models.BooleanField("HR", default=False)
    trainer = models.BooleanField("Trainer", default=False)
    trainee = models.BooleanField("Trainee", default=False)

    def __str__(self):
        return self.full_name


class Module1(models.Model):

    word1 = models.CharField(max_length=250)
    word2 = models.CharField(max_length=250)
    question = models.CharField(max_length=2000)
    right_option = models.CharField(max_length=1000)
    first_wrong_option = models.CharField(max_length=1000)
    second_wrong_option = models.CharField(max_length=1000)
    third_wrong_option = models.CharField(max_length=1000)

    def __str__(self):
        return self.word1


class Module2(models.Model):

    word1 = models.CharField(max_length=250)
    word2 = models.CharField(max_length=250)
    question = models.CharField(max_length=2000)
    right_option = models.CharField(max_length=1000)
    first_wrong_option = models.CharField(max_length=1000)
    second_wrong_option = models.CharField(max_length=1000)
    third_wrong_option = models.CharField(max_length=1000)

    def __str__(self):
        return self.word1


class Module3(models.Model):

    word1 = models.CharField(max_length=250)
    word2 = models.CharField(max_length=250)
    question = models.CharField(max_length=2000)
    right_option = models.CharField(max_length=1000)
    first_wrong_option = models.CharField(max_length=1000)
    second_wrong_option = models.CharField(max_length=1000)
    third_wrong_option = models.CharField(max_length=1000)

    def __str__(self):
        return self.word1


class Module4(models.Model):

    hangman_word = models.CharField(max_length=250)
    question = models.CharField(max_length=2000)
    right_option = models.CharField(max_length=1000)
    first_wrong_option = models.CharField(max_length=1000)
    second_wrong_option = models.CharField(max_length=1000)
    third_wrong_option = models.CharField(max_length=1000)
    explanation = models.CharField(max_length=1000)

    def __str__(self):
        return self.hangman_word


class Module5(models.Model):

    hangman_word = models.CharField(max_length=250)
    question = models.CharField(max_length=2000)
    right_option = models.CharField(max_length=1000)
    first_wrong_option = models.CharField(max_length=1000)
    second_wrong_option = models.CharField(max_length=1000)
    third_wrong_option = models.CharField(max_length=1000)
    explanation = models.CharField(max_length=1000)

    def __str__(self):
        return self.hangman_word


class Hangman(models.Model):
    word = models.CharField(max_length=250)
    word_hint = models.TextField(blank=True, max_length=100)

    def __str__(self):
        return self.word

    class Meta:
        ordering = ["word"]


class Answer(models.Model):
    question_relation = models.ForeignKey(Hangman, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.answer
