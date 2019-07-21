# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:14:32 2019

@author: Sahil
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


google_complete =pd.read_csv("Google.csv")

google_complete['average'] = google_complete[['high','low']].mean(axis=1)

google_complete =google_complete.sort_index(axis = 0,ascending=0)    #sorting by index

google_processed = google_complete.iloc[:, [2,6]].values  

google_training = google_processed[:881,:]    #spliting into test, train
google_testing = google_processed[881:,:]

from sklearn.preprocessing import MinMaxScaler  #Scaling
scaler = MinMaxScaler(feature_range = (0, 1))

google_training_scaled = scaler.fit_transform(google_training)  

features_set = []  
labels = []  
for i in range(50, 881):  
    features_set.append(google_training_scaled[i-50:i,0])                                #50 entries(0-49)
    labels.append(google_training_scaled[i, 0])      

features_set, labels = np.array(features_set), np.array(labels)  

features_set = np.reshape(features_set, (features_set.shape[0], features_set.shape[1], 2))         #reshape into 3d data  (samples, entries in samples, values in entries)

from keras.models import Sequential  
from keras.layers import Dense  
from keras.layers import LSTM  
from keras.layers import Dropout


model = Sequential()

model.add(LSTM(units=50, return_sequences=True, input_shape=(features_set.shape[1], 2)))  #return_sequences=True  if next layer is also LSTM
model.add(Dropout(0.2)) 
model.add(LSTM(units=50, return_sequences=True))  
model.add(Dropout(0.2))

model.add(LSTM(units=50, return_sequences=True))  
model.add(Dropout(0.2))

model.add(LSTM(units=50))  
model.add(Dropout(0.2)) 

model.add(Dense(units = 1))
model.compile(optimizer = 'adam', loss = 'mean_squared_error')

model.fit(features_set, labels, epochs = 100, batch_size = 32)


test_inputs = google_processed[len(google_processed) - len(google_testing) - 50:]


test_inputs = scaler.transform(test_inputs)  

test_features = []  
for i in range(50, 428):  
    test_features.append(test_inputs[i-50:i, 0])

test_features = np.array(test_features)


test_features = np.reshape(test_features, (test_features.shape[0], test_features.shape[1], 1))  


predictions = model.predict(test_features) 

predictions = scaler.inverse_transform(predictions)

plt.figure(figsize=(10,6))  
plt.plot(google_testing, color='blue', label='Actual Google Stock Price')
plt.plot(predictions , color='red', label='Predicted Googlee Stock Price')
plt.title('Google Stock Price Prediction')  
plt.xlabel('Date')  
plt.ylabel('Google Stock Price')  
plt.legend() 
plt.show()

