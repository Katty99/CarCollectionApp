from django.shortcuts import render, redirect

from CarCollectionApp.account.forms import AccountForm, AccountEditForm
from CarCollectionApp.account.models import ProfileModel
from CarCollectionApp.car.models import CarModel


# Create your views here.

def create_profile(request):
    form = AccountForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {'form': form}
    return render(request, template_name='account/profile-create.html', context=context)


def profile_details(request):
    profile = ProfileModel.objects.first()
    total_cost = 0
    cars = CarModel.objects.all()
    for car in cars:
        total_cost += car.price
    context = {'profile': profile, 'total_cost': total_cost}
    return render(request, template_name='account/profile-details.html', context=context)


def edit_profile(request):
    profile = ProfileModel.objects.first()

    if request.method == 'GET':
        context = {'form': AccountEditForm(initial=profile.__dict__)}
        return render(request, template_name='account/profile-edit.html', context=context)

    else:
        form = AccountEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
        else:
            context = {'form': form}
            return render(request, template_name='account/profile-edit.html', context=context)


def delete_profile(request):
    profile = ProfileModel.objects.first()
    cars = CarModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        cars.delete()
        return redirect('home')
    return render(request, template_name='account/profile-delete.html')
