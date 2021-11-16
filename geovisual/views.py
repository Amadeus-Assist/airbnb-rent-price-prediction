from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


def map(request):
    return render(request, 'map.html')


def nyc_geovisual(request):
    csv_data = pd.read_csv('static/data/nyc_stat.csv')
    date = csv_data["Date"].map(lambda x:x[2:10])
    date_list = date.values.tolist()

    avg = csv_data["avg_price"].map(lambda x:str(x))
    avg_list = avg.values.tolist()

    median = csv_data["median_price"].map(lambda x:str(x))
    median_list = median.values.tolist()

    data = {
        "date_list": '|'.join(date_list),
        "avg_list": '|'.join(avg_list),
        "median_list": '|'.join(median_list),
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

