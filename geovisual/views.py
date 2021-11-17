import sys

sys.path.append('housing_price/.')
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from housing_price.covid.query_covid import query_common_request


def map(request):
    return render(request, 'map.html')

def city_view(request, city):
    # csv_data = pd.read_csv('static/data/nyc_stat.csv')
    # date = csv_data["Date"].map(lambda x:x[2:10])
    # datelist_covid = date.values.tolist()

    # avg = csv_data["avg_price"].map(lambda x:str(x))
    # newlist_covid = avg.values.tolist()

    # median = csv_data["median_price"].map(lambda x:str(x))
    # median_list = median.values.tolist()

    coviddata = query_common_request(city, 120)

    datelist_covid = coviddata['date']
    newlist_covid = coviddata['new']

    data = {
        # "date_list": '|'.join(date_list),
        # "avg_list": '|'.join(avg_list),
        # "median_list": '|'.join(median_list),
        "covid_date_list": '|'.join(datelist_covid),
        "covid_new_list": '|'.join(newlist_covid),
        "hotel": "0.9",
        "private": "45.17",
        "entire": "51.47",
        "shared": "2.46",
        "category": "0-100|100-200|200-300|300-400",
        "entire_list": "6.42|24.17|11.04|3.73",
        "private_list": "39.49|8.86|0.94|0.25",
        "hotel_list": "0.11|0.46|0.13|0.12",
        "share_list": "2.27|0.24|0.05|0.02",
        "availability": "81",
        "city": "nyc"
    }

    return render(request, 'geovisual.html', data)

