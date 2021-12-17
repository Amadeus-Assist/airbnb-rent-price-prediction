import pandas as pd 
import os 

def query_sentiment_request(city):
    filepath = os.path.join("city_sentiment_analysis/outputs_new", '{}.csv'.format(city))
    df = pd.read_csv(filepath, header=0)
    data = {'date': [], 'predictions': []}
    for index, row in df.iterrows():
        data['date'].append(row['DateTime'])
        data['predictions'].append(str(row['Score']))
    return data

if __name__ == '__main__':
    print(
        query_sentiment_request(city='nyc')
    )
