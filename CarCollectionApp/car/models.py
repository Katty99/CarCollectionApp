from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from CarCollectionApp.car.validators import year_validation

# Create your models here.
CHOICES = {
    ("Sports Car", "Sports Car"),
    ("Pickup", "Pickup"),
    ("Crossover", "Crossover"),
    ("Minibus", "Minibus"),
    ("Other", "Other")
}


class CarModel(models.Model):
    car_type = models.CharField(max_length=10, choices=CHOICES)
    model = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    year = models.IntegerField(validators=[year_validation])
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(1)])
