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


def covid_single_update(datestr):
    prop = Property_factory.get_instance()
    credential_path = prop['credential_path']
    projectId = prop['project']
    source_path_prefix = prop['covid_source_prefix']
    dest_table = prop['covid_dest_table']
    time_format = '%m-%d-%Y'
    table_time_format = '%Y-%m-%d %H:%M:%S'
    date = dt.strptime(datestr, time_format)
    source_suffix = '.csv'
    df_column = ['date', 'city', 'state', 'country', 'confirmed', 'new']
    citystr = prop['valid_cities']
    valid_cities = parse_city(citystr)
    data_list = []

    credentials = service_account.Credentials.from_service_account_file(
        credential_path)
    pandas_gbq.context.credentials = credentials
    pandas_gbq.context.project = projectId

    prev_date_str = (date - timedelta(1)).strftime(table_time_format) + " UTC"
    SQL = "SELECT C.city, C.confirmed FROM " + dest_table + " C WHERE C.date='" + prev_date_str + "'"
    prev_df = pandas_gbq.read_gbq(SQL)
    prev_confirmed_dict = {}
    for index, row in prev_df.iterrows():
        prev_confirmed_dict[row['city']] = int(row['confirmed'])

    filename = datestr + source_suffix
    path = os.path.join(source_path_prefix, filename)
    df_raw = pandas.read_csv(filepath_or_buffer=path, header=0)

    row_idx = 0
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
            data_list[row_idx].append(
                int(row['Confirmed']) - prev_confirmed_dict[city_name])
            row_idx += 1

    df_sink = pandas.DataFrame(data_list, columns=df_column)
    df_sink['date'] = pandas.to_datetime(df_sink.date)

    pandas_gbq.to_gbq(df_sink,
                      dest_table,
                      project_id=projectId,
                      if_exists='append')


def covid_daily_update():
    time_format = '%m-%d-%Y'
    datestr = (dt.now() - timedelta(1)).strftime(time_format)
    covid_single_update(datestr)


# dend = dt.strptime('2020-12-31', '%Y-%m-%d')
# dstart = dt.strptime('2021-12-09', '%Y-%m-%d')
# l = (dend-dstart).days+1
# for d in range(2):
    # covid_single_update((dstart+timedelta(days=d)).strftime('%m-%d-%Y'))