from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
import pandas_gbq
from housing_price.common.utils import SimilarCityRetriever

def home(request):
    return render(request, 'home.html')

def similar_city(request, city):
    return JsonResponse({'city': SimilarCityRetriever.getSimilarCity(city)})

