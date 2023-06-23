from django.contrib import admin
from django.urls import path, include

from CarCollectionApp.car import views

urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.create_car, name='create_car'),
    path('<int:car_id>/', include([
        path('details/', views.car_details, name='car_details'),
        path('edit/', views.edit_car, name='edit_car'),
        path('delete/', views.delete_car, name='delete_car'),
    ])),
]