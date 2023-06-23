from django.contrib import admin
from django.urls import path, include

from CarCollectionApp.account import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('details/', views.profile_details, name='profile_details'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('delete/', views.delete_profile, name='delete_profile'),
]