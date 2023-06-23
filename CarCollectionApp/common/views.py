from django.shortcuts import render

from CarCollectionApp.account.models import ProfileModel


# Create your views here.

def home(request):
    profile = ProfileModel.objects.first()
    context = {'profile': profile}
    return render(request, template_name='common/index.html', context=context)
