from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.enums import Choices
from django.forms.fields import CharField
from multiselectfield import MultiSelectField

# Create your models here.


class Customer(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'HR'),
        ('HOD', 'HOD'),
        ('Trainer', 'Trainer'),
        ('Trainee', 'Trainee'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField("Full Name", max_length=250)
    email = models.EmailField()
    department = MultiSelectField(choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.full_name

class Module1(models.Model):

    word1 = CharField(max_length=250)
    word2 = CharField(max_length=250)
    question = CharField(max_length=2000)
    right_option = CharField(max_length=1000)
    first_wrong_option = CharField(max_length=1000)
    second_wrong_option = CharField(max_length=1000)
    third_wrong_option = CharField(max_length=1000)

    def __str__(self):
        return self.word1





