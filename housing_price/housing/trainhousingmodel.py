from datetime import datetime, time, timedelta
import sys

import keras
from numpy.lib.function_base import append, insert

sys.path.append('housing_price/.')
from covid.query_covid import query_data_with_length, get_citymap
# from pandas_datareader import data as pdr
import pandas as pd
# import yfinance as yf
import numpy as np
import shutil
import os
from pathlib import Path

from keras import models
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense
from keras.constraints import nonneg
from sklearn.preprocessing import MinMaxScaler
from keras import backend as K

import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams

rcParams['figure.figsize'] = 20, 10
maxcovid = 50000
mincovid = 0
maxhousing = 1000
minhousing = 0
maxemotion = 200
minemotion = 0
maxlen = 365
trainlen = 30
predictlen = 30
rootpath = Path(sys.path[0]).parent.parent.parent
modelpath = os.path.join(rootpath,'model','housing')
citymap = get_citymap()
housingpath = os.path.join(rootpath,'static','data','housing','history')


def trainhousing(city):
    data = query_data_with_length(citymap[city][0], citymap[city][1], citymap[city][2], maxlen)
    housingfilepath = os.path.join(housingpath, 'housing_price_{}.csv'.format(city))
    scorefilepath = os.path.join(housingpath, 'score_{}.csv'.format(city))
    housingdata = pd.read_csv(housingfilepath, header=0)
    scoredata = pd.read_csv(scorefilepath, header=0)
    length = len(data)
    # shiftlen = 30
    yaxisname = 'new'
    xaxisname = 'date'
    # date = [date for date in pandasdata['date']]
    # df = pd.DataFrame(zip(date, pandasdata[yaxisname].values),
    #                 columns=[xaxisname, yaxisname])
    # df.index = df[xaxisname]

    # df = df.sort_index(ascending=True, axis=0)
    # data = pd.DataFrame(index=range(0, len(df)), columns=[xaxisname, yaxisname])
    # for i in range(0, len(data)):
    #     data[xaxisname][i] = df[xaxisname][i]
    #     data[yaxisname][i] = df[yaxisname][i]
    # print(data.head())

    # scaler = MinMaxScaler(feature_range=(0, 1))
    data['housing'] = housingdata['housing']
    data['emotion'] = scoredata['Score']
    data.index = data.date
    data.drop(xaxisname, axis=1, inplace=True)
    train_data = data.values
    train_data = np.append(train_data, [[mincovid, minhousing, minemotion],[maxcovid, maxhousing, maxemotion]], axis=0)
    # print(train_data)
    # train_data = final_data[0:length - predictlen, :]
    # valid_data=final_data[length-predictlen:,:]
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(train_data)[:-2]

    # model_data = scaled_data[-trainlen:]
    # model_data = [model_data]
    # model_data = np.asarray(model_data)
    # model_data = np.reshape(model_data, (model_data.shape[0], model_data.shape[1], 3))
    
    # model_data = model_data.reshape(-1, 1)
    # model_data = scaler.transform(model_data)

    # # X_test = [model_data]
    # # X_test = np.array(X_test)
    # # X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    for sl in range(1, predictlen + 1):
        x_train_data, y_train_data = [], []
        for i in range(0, length - trainlen - sl):
            x_train_data.append(scaled_data[i:i + trainlen, 0:3])
            y_train_data.append(scaled_data[i + trainlen + sl - 1, 1])
        x_train_data = np.asarray(x_train_data)
        y_train_data = np.asarray(y_train_data)
        x_train_data = np.reshape(x_train_data, (x_train_data.shape[0], x_train_data.shape[1], 3))
        # print(x_train_data)

        lstm_model = Sequential()
        lstm_model.add(
            LSTM(units=50,
                return_sequences=True,
                input_shape=(np.shape(x_train_data)[1], 3)))
        lstm_model.add(LSTM(units=50))
        lstm_model.add(Dense(1, kernel_constraint=nonneg()))
        # print(model_data)
        # print('len of model_data: {}'.format(len(model_data)))

        lstm_model.compile(loss='mean_squared_error', optimizer='adam')
        # print(x_train_data)
        # x_train_data = np.array(x_train_data)
        # y_train_data = np.array(y_train_data)
        # print('--------------------------')
        # print(y_train_data)
        for i in range(5):
            lstm_model.fit(x_train_data,
                        y_train_data,
                        epochs=1,
                        batch_size=1,
                        verbose=2)
        
        # predicted = lstm_model.predict(model_data)
        # predicted = [np.append(predicted[0],[0,0])]
        # predicted = np.asarray(predicted)
        # predicted = scaler.inverse_transform(predicted)
        # print(predicted)


        localmodelpath = os.path.join(modelpath, 'city_{}'.format(city), 'predictlen_{}'.format(sl))
        if os.path.exists(localmodelpath):
            for file in os.listdir(localmodelpath):
                filepath = os.path.join(localmodelpath, file)
                if os.path.isfile(filepath):
                    os.remove(filepath)
                else:
                    shutil.rmtree(filepath)
        else:
            os.makedirs(localmodelpath)
        lstm_model.save(os.path.join(localmodelpath, 'model.h5'))


def predicthousing(city):
    data = query_data_with_length(citymap[city][0], citymap[city][1], citymap[city][2], trainlen)
    housingfilepath = os.path.join(housingpath, 'housing_price_{}.csv'.format(city))
    scorefilepath = os.path.join(housingpath, 'score_{}.csv'.format(city))
    housingdata = pd.read_csv(housingfilepath, header=0)[-trainlen:]
    scoredata = pd.read_csv(scorefilepath, header=0)[-trainlen:]
    housingdata.index = data.index
    scoredata.index = data.index
    # print(housingdata)
    length = len(data)
    yaxisname = 'new'
    xaxisname = 'date'
    td = datetime.now()
    date = []
    for i in range(predictlen):
        date.append((td+timedelta(days=i)).strftime('%m-%d'))
    predictdata = pd.DataFrame(date,
                    columns=[xaxisname])
    predictdata.index = predictdata.date
    predictdata.drop(xaxisname, axis=1, inplace=True)
    # date = [date for date in pandasdata['date']]
    # df = pd.DataFrame(zip(date, pandasdata[yaxisname].values),
    #                 columns=[xaxisname, yaxisname])
    # df.index = df[xaxisname]

    # df = df.sort_index(ascending=True, axis=0)
    # data = pd.DataFrame(index=range(0, len(df)), columns=[xaxisname, yaxisname])
    # for i in range(0, len(data)):
    #     data[xaxisname][i] = df[xaxisname][i]
    #     data[yaxisname][i] = df[yaxisname][i]
    # print(data.head())

    # scaler = MinMaxScaler(feature_range=(0, 1))
    data['housing'] = housingdata['housing']
    data['emotion'] = scoredata['Score']
    data.index = data.date
    data.drop(xaxisname, axis=1, inplace=True)
    test_data = data.values
    test_data = np.append(test_data, [[mincovid, minhousing, minemotion],[maxcovid, maxhousing, maxemotion]], axis=0)
    scaler = MinMaxScaler(feature_range=(0, 1))
    model_data = scaler.fit_transform(test_data)[:-2]

    X_test = [model_data]
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 3))
    
    predicted_res = []
    for sl in range(1, predictlen + 1):
        localmodelpath = os.path.join(modelpath, 'city_{}'.format(city), 'predictlen_{}'.format(sl),'model.h5')
        lstm_model=models.load_model(localmodelpath)

        predicted = lstm_model.predict(X_test)
        predicted = np.insert(predicted, 0, 0, axis=1)
        predicted = np.insert(predicted, 2, 0, axis=1)
        # predicted = [np.append(predicted[0],[0,0])]
        # predicted = np.asarray(predicted)
        predicted = scaler.inverse_transform(predicted)
        predicted_res.append(0 if predicted[0][1]==0 else round(predicted[0][1],2))
        
    predictdata['predictions'] = predicted_res
    savepath = os.path.join(rootpath, 'static', 'data', 'housing', 'predict')
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    savefilepath = os.path.join(savepath, 'city_{}.csv'.format(city))
    predictdata.to_csv(savefilepath, mode='w')
    # plt.plot(predictdata['Predictions'], label='predictions')
    # plt.legend()
    # plt.show()

# trainhousing('nyc')
# predicthousing('nyc')


# days = 430
# pandasdata = query_data_with_city('nyc', days)
# print(pandasdata.head())
# length = len(pandasdata)
# trainlen = 30
# predictlen = 1
# # shiftlen = 30
# yaxisname = 'new'
# xaxisname = 'Date'
# date = [date for date in pandasdata['date']]
# df = pd.DataFrame(zip(date, pandasdata[yaxisname].values),
#                   columns=[xaxisname, yaxisname])
# print(df.head())
# df.index = df[xaxisname]

# df = df.sort_index(ascending=True, axis=0)
# data = pd.DataFrame(index=range(0, len(df)), columns=[xaxisname, yaxisname])
# for i in range(0, len(data)):
#     data[xaxisname][i] = df[xaxisname][i]
#     data[yaxisname][i] = df[yaxisname][i]
# print(data.head())

# scaler = MinMaxScaler(feature_range=(0, 1))
# data.index = data.Date
# data.drop(xaxisname, axis=1, inplace=True)
# print(data.head())
# final_data = data.values
# final_data = np.append(final_data,[[0],[50000]],axis=0)
# train_data = final_data[0:length - predictlen, :]
# # valid_data=final_data[length-predictlen:,:]
# scaler = MinMaxScaler(feature_range=(0, 1))
# scaled_data = scaler.fit_transform(final_data)
# final_data=final_data[:-2]
# scaled_data=scaled_data[:-2]

# model_data = data[len(data) - predictlen - trainlen:len(data) -
#                   predictlen].values
# # print('model_data_before reshape: {}'.format(model_data))
# model_data = model_data.reshape(-1, 1)
# # print('model_data_after reshape: {}'.format(model_data))
# model_data = scaler.transform(model_data)
# # print('model_data: {}'.format(model_data))

# X_test = [model_data]
# X_test = np.array(X_test)
# X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
# # print('X_test: {}'.format(X_test))

# predicted_res = []

# for sl in range(1, predictlen + 1):
#     x_train_data, y_train_data = [], []
#     for i in range(0, len(train_data) - trainlen - sl):
#         x_train_data.append(scaled_data[i:i + trainlen, 0])
#         y_train_data.append(scaled_data[i + trainlen + sl - 1, 0])
#     x_train_data = np.asarray(x_train_data)
#     y_train_data = np.asarray(y_train_data)
#     x_train_data = np.reshape(
#         x_train_data, (x_train_data.shape[0], x_train_data.shape[1], 1))

#     lstm_model = Sequential()
#     lstm_model.add(
#         LSTM(units=50,
#              return_sequences=True,
#              input_shape=(np.shape(x_train_data)[1], 1)))
#     lstm_model.add(LSTM(units=50))
#     lstm_model.add(Dense(1, kernel_constraint=nonneg()))
#     # print(model_data)
#     # print('len of model_data: {}'.format(len(model_data)))

#     lstm_model.compile(loss='mean_squared_error', optimizer='adam')
#     # print(x_train_data)
#     # x_train_data = np.array(x_train_data)
#     # y_train_data = np.array(y_train_data)
#     # print('--------------------------')
#     # print(y_train_data)
#     for i in range(10):
#         lstm_model.fit(x_train_data,
#                        y_train_data,
#                        epochs=1,
#                        batch_size=1,
#                        verbose=2)
#         # lstm_model.reset_states()

#     predicted_stock_price = lstm_model.predict(X_test)
#     predicted_stock_price = scaler.inverse_transform(predicted_stock_price)
#     predicted_res.append(predicted_stock_price[0][0])
#     K.clear_session()

# train_data = data[:length - predictlen]
# valid_data = data[length - predictlen:]
# valid_data['Predictions'] = predicted_res
# plt.plot(train_data[yaxisname], label='Train Data')
# plt.plot(valid_data[[yaxisname, "Predictions"]],
#          label=['Valid Data', 'Prediction Data'])
# plt.legend()
# plt.show()