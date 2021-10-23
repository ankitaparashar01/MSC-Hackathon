from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.enums import Choices
from multiselectfield import MultiSelectField

# Create your models here.


class Customer(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'HR'),
        ('HOD', 'HOD'),
        ('Trainer', 'Trainer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField("Full Name", max_length=250)
    email = models.EmailField()
    department = MultiSelectField(choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.full_name
