import urllib.parse
import urllib.request
from tweepy.streaming import json
import datetime
import csv
import os

from config import OUTPUT_PATH, GOOGLE_MAP_API_KEY


def get_geocode(city):
    data = {}
    data['address'] = city
    # url_values
    url_values = urllib.parse.urlencode(data)
    print(url_values)

    # url_values
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    full_url = url + '?' + url_values + '&key=' + GOOGLE_MAP_API_KEY
    print(full_url)

    # response
    data = urllib.request.urlopen(full_url)
    response = json.load(data)
    print(response)

    # latitude
    latitude = response['results'][0]['geometry']['location']['lat']
    print('lat: ', latitude)

    # longitude
    longitude = response['results'][0]['geometry']['location']['lng']
    print('lng: ', longitude)

    # geocode
    radius_km = 20
    geocode = str(float(latitude)) + ',' + str(float(longitude)
                                               ) + ',' + str(float(radius_km)) + 'km'
    print("geocode", geocode)
    return geocode


def write_to_csv(table_name, score):
    file_name = os.path.join(OUTPUT_PATH, table_name + '_score.csv')
    if os.path.exists(file_name):
        with open(file_name, 'a', newline='') as csvfile:
            csv_writer = csv.writer(
                csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(
                (datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"), score))
    else:
        with open(file_name, 'w', newline='') as csvfile:
            csv_writer = csv.writer(
                csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['DateTime', 'Score'])
            csv_writer.writerow(
                (datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"), score))
