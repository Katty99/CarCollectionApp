from django import forms

from CarCollectionApp.car.models import CarModel


class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
