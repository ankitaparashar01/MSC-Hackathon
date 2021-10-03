from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

department_choices = (
    ('HR', 'HR'),
    ('Trainee', 'Trainee'),
    ('IDK', 'IDK'),
)
role_choices = (
    ('role1', 'role1'),
    ('role2', 'role2'),
    ('role3', 'role3'),
)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField("Full Name", max_length=250)
    email = models.EmailField()
    department = models.CharField(max_length=250,
                                  choices=department_choices,
                                  default='HR')
    role = models.CharField(max_length=250,
                            choices=role_choices,
                            default='role1')

    def __str__(self):
        return self.full_name
