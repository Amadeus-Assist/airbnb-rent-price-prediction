import sys

import keras

sys.path.append('housing_price/.')
from covid.query_covid import query_data_with_city
# from pandas_datareader import data as pdr
import pandas as pd
# import yfinance as yf
import numpy as np

from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense
from keras.constraints import nonneg
from sklearn.preprocessing import MinMaxScaler
from keras import backend as K

import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams

rcParams['figure.figsize'] = 20, 10

days = 430
pandasdata = query_data_with_city('nyc', days)
length = len(pandasdata)
trainlen = 30
predictlen = 120
# shiftlen = 30
yaxisname = 'new'
xaxisname = 'Date'
date = [date for date in pandasdata['date']]
df = pd.DataFrame(zip(date, pandasdata[yaxisname].values),
                  columns=[xaxisname, yaxisname])
df.index = df[xaxisname]

df = df.sort_index(ascending=True, axis=0)
data = pd.DataFrame(index=range(0, len(df)), columns=[xaxisname, yaxisname])
for i in range(0, len(data)):
    data[xaxisname][i] = df[xaxisname][i]
    data[yaxisname][i] = df[yaxisname][i]
# print(data.head())

scaler = MinMaxScaler(feature_range=(0, 1))
data.index = data.Date
data.drop(xaxisname, axis=1, inplace=True)
final_data = data.values
train_data = final_data[0:length - predictlen, :]
# valid_data=final_data[length-predictlen:,:]
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(final_data)

model_data = data[len(data) - predictlen - trainlen:len(data) -
                  predictlen].values
model_data = model_data.reshape(-1, 1)
model_data = scaler.transform(model_data)

X_test = [model_data]
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

predicted_res = []

for sl in range(1, predictlen + 1):
    x_train_data, y_train_data = [], []
    for i in range(0, len(train_data) - trainlen - sl):
        x_train_data.append(scaled_data[i:i + trainlen, 0])
        y_train_data.append(scaled_data[i + trainlen + sl - 1, 0])
    x_train_data = np.asarray(x_train_data)
    y_train_data = np.asarray(y_train_data)
    x_train_data = np.reshape(
        x_train_data, (x_train_data.shape[0], x_train_data.shape[1], 1))

    lstm_model = Sequential()
    lstm_model.add(
        LSTM(units=50,
             return_sequences=True,
             input_shape=(np.shape(x_train_data)[1], 1)))
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
    for i in range(10):
        lstm_model.fit(x_train_data,
                       y_train_data,
                       epochs=1,
                       batch_size=1,
                       verbose=2)
        # lstm_model.reset_states()

    predicted_stock_price = lstm_model.predict(X_test)
    predicted_stock_price = scaler.inverse_transform(predicted_stock_price)
    predicted_res.append(predicted_stock_price[0][0])
    K.clear_session()

train_data = data[:length - predictlen]
valid_data = data[length - predictlen:]
valid_data['Predictions'] = predicted_res
plt.plot(train_data[yaxisname], label='Train Data')
plt.plot(valid_data[[yaxisname, "Predictions"]],
         label=['Valid Data', 'Prediction Data'])
plt.legend()
plt.show()