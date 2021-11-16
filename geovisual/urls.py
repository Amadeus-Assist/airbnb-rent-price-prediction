from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('nyc', views.nyc_geovisual, name='nyc'),
]