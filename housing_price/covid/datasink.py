import sys

sys.path.append('housing_price/.')
from common.utils import Property_factory
from datetime import datetime as dt, timedelta
import pandas
import pandas_gbq
from google.oauth2 import service_account
import os


def parse_city(citystr):
    res = set()
    citystr = citystr[1:len(citystr) - 1]
    cc = citystr.split('),(')
    for tp in cc:
        tps = tp.split(',')
        res.add((tps[0].strip(), tps[1].strip(), tps[2].strip()))
    return res


prop = Property_factory.get_instance()
credential_path = prop['credential_path']
projectId = prop['project']
bucket = prop['covid_bucket']
source_path_prefix = prop['covid_source_prefix']
data_range = prop['covid_date_range']
dest_table = prop['covid_dest_table']
time_format = '%m-%d-%Y'
source_suffix = '.csv'
df_column = ['date', 'city', 'state', 'country', 'confirmed', 'new']
citystr = prop['valid_cities']
valid_cities = parse_city(citystr)
data_list = []

credentials = service_account.Credentials.from_service_account_file(
    credential_path)
pandas_gbq.context.credentials = credentials
pandas_gbq.context.project = projectId

if data_range.find('/') != -1:
    sp = data_range.find('/')
    start_date = dt.strptime(data_range[0:sp].strip(), time_format)
    end_date = dt.strptime(data_range[sp + 1:].strip(), time_format)
else:
    today = dt.now().strftime(time_format)
    end_date = today - dt.timedelta(1)
    start_date = today - dt.timedelta(data_range)

days = (end_date - start_date).days + 1
row_idx = 0
for i in range(days):
    timestamp = start_date + timedelta(i)
    datestr = timestamp.strftime(time_format)
    filename = datestr + source_suffix
    path = os.path.join(source_path_prefix, filename)
    df_raw = pandas.read_csv(filepath_or_buffer=path, header=0)
    for index, row in df_raw.iterrows():
        if pandas.isna(row['Admin2']):
            city_name = row['Province_State']
        else:
            city_name = row['Admin2']
        if (city_name, row['Province_State'],
                row['Country_Region']) in valid_cities:
            data_list.append([])
            data_list[row_idx].append(datestr)
            data_list[row_idx].append(city_name)
            data_list[row_idx].append(row['Province_State'])
            data_list[row_idx].append(row['Country_Region'])
            data_list[row_idx].append(int(row['Confirmed']))
            data_list[row_idx].append(0)
            if row_idx >= len(valid_cities):
                data_list[row_idx][5] = data_list[row_idx][4] - data_list[
                    row_idx - len(valid_cities)][4]
            row_idx += 1

df_sink = pandas.DataFrame(data_list, columns=df_column)
df_sink['date'] = pandas.to_datetime(df_sink.date)

pandas_gbq.to_gbq(df_sink,
                  dest_table,
                  project_id=projectId,
                  if_exists='replace')