import pandas as pd 
import os 

# Google map API key
GOOGLE_MAP_API_KEY = 'AIzaSyBK99p_AsbBHJcuCQLOxzCtR1clDl7D-ko'

# Twitter Credentials
ACCESS_TOKEN = "1133350537204834305-Wft7EpVTfwLgYSfJQdH2gzxiEfsP9o"
ACCESS_TOKEN_SECRET = "gme5J65D28mA4wdISfPaaKQqmhFZUqJAwXtguiJRbcgn4"
CONSUMER_KEY = "Ej6ZAEym4PWa5BRtxSepTOaM0"
CONSUMER_SECRET = "tbBwCbrG4xq5z4In3B6N76WJh6Iox1fMwAnk2sxJb3Silnxp2M"

# all the city names
uscities_table = pd.read_csv("resource/uscities.csv")
CITY_LIST = list(uscities_table["city"])[1:3]

# Path settings
OUTPUT_PATH = './outputs'