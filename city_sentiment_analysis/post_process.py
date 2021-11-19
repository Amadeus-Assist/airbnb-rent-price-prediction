from numpy.core.fromnumeric import mean, var
import pandas as pd
import os
import datetime
import numpy as np 

from config import CITY_LIST


def str_2_datetime(s, format="%Y-%m-%d-%H-%M"):
    return datetime.datetime.strptime(s, format=format)

def get_score_features():
    scores = []
    local_path = './outputs'
    file_names = os.listdir(local_path)
    for file_name in file_names:
        table_path = os.path.join(local_path, file_name)
        df = pd.read_csv(
            table_path
        )
        scores += list(df['Score'])
    scores = np.array(scores)
    return np.mean(scores), np.var(scores), np.std(scores)


def assess_score(start="0000-00-00-00-00", end="9999-12-31-23-59", city="New York"):
    avg, v, s = get_score_features()
    s = s / 2
    df = statistics_by_datetime_city(start, end, city)
    scores = list(df['Score'])
    final_score = sum(scores) / len(scores)
    diff = final_score - avg
    if diff == 0:
        return "-"
    elif diff > 0 and diff <= s:
        return "fine"
    elif diff > s and diff <= 2 * s:
        return "good"
    elif diff > 2 * s and diff <= 3 * s:
        return "very good"
    elif diff > 3 * s:
        return "excellent"
    elif diff < 0 and diff >= -s:
        return "not bad"
    elif diff < -s and diff >= -2 * s:
        return "not good"
    elif diff < -2 * s and diff >= -3 * s:
        return "bad"
    elif diff < -3 * s:
        return "poor"
    else:
        return

def statistics_by_datetime_city(start="0000-00-00-00-00", end="9999-12-31-23-59", city="New York"):

    local_path = './outputs'
    table_name = str.replace(city, " ", "_", )
    table_path = os.path.join(local_path, table_name + '_score.csv')

    df = pd.read_csv(
        table_path,
    )

    return df.loc[(df['DateTime'] >= start) & (df['DateTime'] <= end)]


def main():
    # print(statistics_by_datetime_city(
    #     start="2021-11-18-03-39", end="2021-11-18-03-43", city="New York"))
    print(assess_score(start="2021-11-18-03-39", end="2021-11-18-03-43", city="Shanghai"))
    return 0


if __name__ == '__main__':
    main()
