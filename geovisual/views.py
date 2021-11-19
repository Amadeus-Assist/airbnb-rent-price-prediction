import sys

sys.path.append('housing_price/.')
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from housing_price.covid.query_covid import query_common_request
from django.http.response import JsonResponse
from housing_price.common.utils import getPicList


def map(request):
    return render(request, 'map.html')

def city_view(request, city):
    # render housing price chart
    housingData = pd.read_csv('static/data/' + city + '_stat.csv')
    date = housingData["Date"].map(lambda x:x[2:10])
    date_list = date.values.tolist()

    housingAvg = housingData["avg_price"].map(lambda x:str(x))
    avg_list = housingAvg.values.tolist()

    housingMedian = housingData["median_price"].map(lambda x:str(x))
    median_list = housingMedian.values.tolist()

    # reder covid chart
    coviddata = query_common_request(city, 270)

    datelist_covid = coviddata['date']
    newlist_covid = coviddata['new']

    data = {
        "date_list": '|'.join(date_list),
        "avg_list": '|'.join(avg_list),
        "median_list": '|'.join(median_list),
        "covid_date_list": '|'.join(datelist_covid),
        "covid_new_list": '|'.join(newlist_covid),
        "city": city
    }

    return render(request, 'geovisual.html', data)

def get_pic_list(request, city):
    return JsonResponse({'pic': getPicList(city)})

