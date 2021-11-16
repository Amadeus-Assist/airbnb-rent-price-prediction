from django.http import HttpResponse
from django.shortcuts import render
import pandas_gbq
from google.oauth2 import service_account


# Make sure you have installed pandas-gbq at first;
# You can use the other way to query BigQuery.
# please have a look at
# https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-nodejs
# To get your credential

# credentials = service_account.Credentials.from_service_account_file('/Users/gmx15/workspace/hw4_tutorial/bigData-0bd1099b6ed0.json')


def home(request):
    return render(request, 'home.html')
