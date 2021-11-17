from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.map, name='map'),
    re_path(r'^cityview/(?P<city>\w+)$', views.city_view, name='cityview'),
]