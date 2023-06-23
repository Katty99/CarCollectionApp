from django.shortcuts import render, redirect

from CarCollectionApp.car.forms import CarForm
from CarCollectionApp.car.models import CarModel


# Create your views here.
def catalogue(request):
    cars = CarModel.objects.all()
    total_cars = len(cars)
    context = {'cars': cars, 'total_cars': total_cars}
    return render(request, template_name='car/catalogue.html', context=context)


def create_car(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    context = {'form': form}
    return render(request, template_name='car/car-create.html', context=context)


def car_details(request, car_id):
    car = CarModel.objects.get(id=car_id)
    context = {'car': car}
    return render(request, template_name='car/car-details.html', context=context)


def edit_car(request, car_id):
    car = CarModel.objects.get(id=car_id)
    if request.method == 'GET':
        context = {'form': CarForm(initial=car.__dict__)}
        return render(request, template_name='car/car-edit.html', context=context)
    else:
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            context = {'form': form}
            return render(request, template_name='car/car-edit.html', context=context)


def delete_car(request, car_id):
    car = CarModel.objects.get(id=car_id)
    if request.method == "POST":
        car.delete()
        return redirect('catalogue')
    return render(request, template_name='car/car-delete.html')
