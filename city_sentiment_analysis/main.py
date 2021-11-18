#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Columbia EECS E6893 Big Data Analytics

"""
This sub-project does the following:
--------------------------------
1. Get geocode for user provided city name
2. Connect to Twitter and run geo-query
3. Assign a score to each polled tweet using TextBlob
4. Calculate average score for polled tweets
5. Write score and datetime to CSV file
6. Push score to BigQuery
"""

import time
import datetime

from utils import get_geocode
from twitter_stream import get_tweets
from utils import write_to_csv
from config import OUTPUT_PATH
from config import CITY_LIST


def get_geocodes_dict(cities):
    res = {}
    for city in cities:
        res[city] = get_geocode(city=city)
    return res


if __name__ == '__main__':

    city_list = CITY_LIST

    geocodes_dict = get_geocodes_dict(city_list)

    while True:
        try:
            for city in city_list:
                geocode = geocodes_dict.get(city, None)
                score = get_tweets(geocode)
                print(datetime.datetime.now().strftime(
                    "%Y-%m-%d-%H-%M") + ": " + str(float(score)))
                tableName = str.replace(city, " ", "_", )
                write_to_csv(tableName, score)
        except:
            print("There was a problem fetching data from Twitter.")
        finally:
            time.sleep(60)
