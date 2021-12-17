import sys

sys.path.append('housing_price/.')
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from housing_price.covid.query_covid import query_common_request, query_prediction_request
from housing_price.covid.query_housing import query_housing_prediction_request
from housing_price.housing.queryanalysisimgs import queryanalysispath

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
    coviddata = query_common_request(city)

    datelist_covid = coviddata['date']
    newlist_covid = coviddata['new']

    covidpredictdata = query_prediction_request(city)
    datelist_covid_predict = covidpredictdata['date']
    newlist_covid_predict = covidpredictdata['predictions']

    housingpredictdata = query_housing_prediction_request(city)
    datelist_housing_predict = housingpredictdata['date']
    housing_predict = housingpredictdata['predictions']

    data = {
        "date_list": '|'.join(date_list),
        "avg_list": '|'.join(avg_list),
        "median_list": '|'.join(median_list),
        "covid_date_list": '|'.join(datelist_covid),
        "covid_new_list": '|'.join(newlist_covid),
        "covid_date_list_predict": '|'.join(datelist_covid_predict),
        "covid_new_list_predict": '|'.join(newlist_covid_predict),
        "housing_date_list_predict": '|'.join(datelist_housing_predict),
        "housing_predict": '|'.join(housing_predict),
        "city": city
    }

    return render(request, 'geovisual.html', data)

