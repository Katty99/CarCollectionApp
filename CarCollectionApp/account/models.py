from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from CarCollectionApp.account.validators import min_length_validator


class ProfileModel(models.Model):
    username = models.CharField(max_length=10, validators=[min_length_validator, ])
    email_address = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(18), ])
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)
