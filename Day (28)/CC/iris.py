# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:42:35 2019

@author: Sahil
"""

import numpy as np 
import pandas as pd 


import pandas as pd
iris_test = pd.read_csv("iris_test.csv")
iris_train = pd.read_csv("iris_training.csv")

features_train = iris_train.iloc[:, 0:4].values
labels_train = iris_train.iloc[:, 4:].values

features_test = iris_train.iloc[:, 0:4].values
labels_test = iris_train.iloc[:, 4:].values


#one hot encoding on labels train
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder()
labels_train = onehotencoder.fit_transform(labels_train).toarray()

#labels_train = onehotencoder.fit_transform(labels_train.reshape(-1,1)).toarray()

#labels_train = labels_train[:, 1:]



#one hot encoding on labels test
labels_test = onehotencoder.fit_transform(labels_test).toarray()

#labels_train = onehotencoder.fit_transform(labels_train.reshape(-1,1)).toarray()

#labels_test = labels_test[:, 1:]

"""
from keras.utils import np_utils
# Encoding training dataset (one hot encoding of label_train)
encoding_labels_train = np_utils.to_categorical(labels_train)

# Encoding training dataset  (one hot encoding of label_test)
encoding_labels_test = np_utils.to_categorical(labels_test)

encoding_labels_train[0]
"""

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

# Creating a model
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compiling model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training a model
model.fit(features_train, labels_train, epochs=300, batch_size=10)

# Evaluate the model
scores = model.evaluate(features_test, labels_test)
print("\nAccuracy: %.2f%%" % (scores[1]*100))

model.summary()

model.count_params()


"""
labels_pred = model.predict(features_test)
labels_pred = (labels_pred > 0.5)

labels_pred

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

cm
"""