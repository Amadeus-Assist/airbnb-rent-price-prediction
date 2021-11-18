import pandas as pd 
import os 

# Google map API key
GOOGLE_MAP_API_KEY = ''

# Twitter Credentials
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

# all the city names
uscities_table = pd.read_csv("resource/uscities.csv")
CITY_LIST = list(uscities_table["city"])[1:3]

# Path settings
OUTPUT_PATH = './outputs'