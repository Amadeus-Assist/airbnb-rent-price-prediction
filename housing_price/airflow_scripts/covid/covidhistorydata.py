import sys
sys.path.append('housing_price/.')
from covid.query_covid import query_data_with_length
from common.utils import Property_factory
from covid.dailyupdate import parse_city
from datetime import datetime as dt
from pathlib import Path
import os

nickmap = {
    'New York': 'nyc',
    'Los Angeles': 'la',
    'Cook': 'chicago',
}

prop = Property_factory.get_instance()
citydict = parse_city(prop['valid_cities'])
showdays = 270
rootpath = Path(sys.path[0]).parent.parent.parent
savepath = os.path.join(rootpath, 'static', 'data', 'covid', 'history')
if not os.path.exists(savepath):
    os.makedirs(savepath)


for citytuple in citydict.values():
    df = query_data_with_length(citytuple[0], citytuple[1], citytuple[2], showdays)
    df['date'] = df['date'].dt.strftime('%m-%d')
    savefilepath = os.path.join(savepath, 'city_history_{}.csv'.format(nickmap[citytuple[0]]))
    df.to_csv(savefilepath, mode='w', index=False)
    


