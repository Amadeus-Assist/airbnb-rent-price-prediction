from django.http import HttpResponse
from django.shortcuts import render
import pandas_gbq

def home(request):
    return render(request, 'home.html')
