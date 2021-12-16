import sys

sys.path.append('housing_price/.')
from pathlib import Path
import os
import pandas as pd

citymap = {
    'nyc': ('New York', 'New York', 'US'),
    'la': ('Los Angeles', 'California', 'US'),
    'sh': ('Shanghai', 'Shanghai', 'China'),
    'chicago': ('Cook', 'Illinois', 'US'),
}
rootpath = Path(sys.path[0])
housingpath = os.path.join(rootpath, 'static', 'data', 'housing')

def query_housing_prediction_request(city):
    filepath = os.path.join(housingpath, 'predict', 'city_{}.csv'.format(city))
    df = pd.read_csv(filepath, header=0)
    data = {'date': [], 'predictions': []}
    for index, row in df.iterrows():
        data['date'].append(row['date'])
        data['predictions'].append(str(row['predictions']))
    return data