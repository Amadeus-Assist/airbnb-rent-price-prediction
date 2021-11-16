import sys

sys.path.append('housing_price/.')
from common.utils import Property_factory
from datetime import datetime as dt
import pandas_gbq
from google.oauth2 import service_account

time_format = '%m-%d-%Y'
table_time_format = '%Y-%m-%d %H:%M:%S'
prop = Property_factory.get_instance()
credential_path = prop['credential_path']
projectId = prop['project']
credentials = service_account.Credentials.from_service_account_file(
    credential_path)
pandas_gbq.context.credentials = credentials
pandas_gbq.context.project = projectId


def query_common_data(city, state, country, date_start, date_end):
    source_table = prop['covid_dest_table']
    dateStart = dt.strptime(date_start.strip(),
                            time_format).strftime(table_time_format) + ' UTC'
    dateEnd = dt.strptime(date_end.strip(),
                          time_format).strftime(table_time_format) + ' UTC'
    SQL = "SELECT C.date, C.new FROM {} C WHERE C.date BETWEEN @dateStart AND @dateEnd"\
        " AND C.city=@city AND C.state=@state AND C.country=@country ORDER BY C.date".format(source_table)
    query_config = {
        'query': {
            'parameterMode': 'NAMED',
            'queryParameters': [
                {
                    'name': 'source_table',
                    'parameterType': {'type': 'STRING'},
                    'parameterValue': {'value': source_table}
                },{
                    'name': 'dateStart',
                    'parameterType': {'type': 'TIMESTAMP'},
                    'parameterValue': {'value': dateStart}
                },{
                    'name': 'dateEnd',
                    'parameterType': {'type': 'TIMESTAMP'},
                    'parameterValue': {'value': dateEnd}
                },{
                    'name': 'city',
                    'parameterType': {'type': 'STRING'},
                    'parameterValue': {'value': city}
                },{
                    'name': 'state',
                    'parameterType': {'type': 'STRING'},
                    'parameterValue': {'value': state}
                },{
                    'name': 'country',
                    'parameterType': {'type': 'STRING'},
                    'parameterValue': {'value': country}
                }
            ]
        }
    }
    df = pandas_gbq.read_gbq(SQL, configuration=query_config)
    df['date'] = df['date'].dt.strftime(time_format)
    data = []
    for index, row in df.iterrows():
        data.append({'date': row['date'], 'new': row['new']})
    return data


# data = query_common_data('Shanghai', 'Shanghai', 'China', '05-04-2021',
#                          '06-02-2021')
# print(data)
