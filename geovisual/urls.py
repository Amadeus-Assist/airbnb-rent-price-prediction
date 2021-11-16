from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('nyc', views.vis_nyc, name='nyc'),
    path('london', views.vis_london, name='london'),
    path('beijing', views.vis_beijing, name='beijing'),
    path('paris', views.vis_paris, name='paris'),
    path('tokyo', views.vis_tokyo, name='tokyo'),
]