from django.contrib import admin
from django.urls import path, include

from CarCollectionApp.common import views

urlpatterns = [
    path('', views.home, name='home'),
]