# -*- coding: utf-8 -*-
"""DL-Intro-ANN-Churn-Modeling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uY4i2hQsoDpWLS0_VlKi40F5iyk48AXQ
"""

from google.colab import drive
drive.mount('/content/drive')

import os
os.getcwd()

os.chdir('/content/drive/My Drive/App')

import pandas as pd
dataset = pd.read_csv("Churn_Modelling.csv")

dataset.shape

dataset.head()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

features = dataset.iloc[:, 3:13].values
labels = dataset.iloc[:, 13].values

features[1]

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_features_1 = LabelEncoder()
features[:, 1] = labelencoder_features_1.fit_transform(features[:, 1])

labelencoder_features_2 = LabelEncoder()
features[:, 2] = labelencoder_features_2.fit_transform(features[:, 2])

onehotencoder = OneHotEncoder(categorical_features = [1])
features = onehotencoder.fit_transform(features).toarray()

features = features[:, 1:] #dummy variable trap

features[1]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

features.shape

#adding the first hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))

# Adding the second hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

classifier.fit(features_train, labels_train, batch_size = 10, epochs = 10)

labels_pred = classifier.predict(features_test)
labels_pred = (labels_pred > 0.5)

len(labels_pred)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

cm

"""# Lets summarize the above model."""

print classifier.summary()

classifier.count_params()

!pip install pydot

!pip install pydot_ng

!pip install graphviz

!pip install pydotplus

!pip install pydot==1.2.3

import pydot
from keras.utils.vis_utils import plot_model

pydot.__version__

#check out the issue, the code is not working
plot_model(classifier, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

#check out the issue, the code is not working
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

SVG(model_to_dot(classifier).create(prog='dot', format='svg'))

classifier.layers

for layer in classifier.layers:
    print layer.input_shape #how the input data is coming to hidden/dense layers

"""You can get to know that: there is no activation function present "in" the first layer neurons at all. the very first layer is your raw data so no activation function. 

The next layer (i.e. the 1st hidden layer) applies the activation function as well as all subsequent layers.
"""

for layer in classifier.layers:
    print layer.output_shape

"""# Classification using Iris Dataset"""

# Importing libraries
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy
import pandas as pd

training_dataset = pd.read_csv('/content/drive/My Drive/App/iris_training.csv')
features_train = training_dataset.iloc[:, 0:4].values
labels_train = training_dataset.iloc[:, 4].values

training_dataset.head()



# Import testing dataset
test_dataset = pd.read_csv('/content/drive/My Drive/App/iris_test.csv')
features_test = test_dataset.iloc[:, 0:4].values
labels_test = test_dataset.iloc[:, 4].values

test_dataset.sample()

# Encoding training dataset (one hot encoding of label_train)
encoding_labels_train = np_utils.to_categorical(labels_train)

# Encoding training dataset  (one hot encoding of label_test)
encoding_labels_test = np_utils.to_categorical(labels_test)

encoding_labels_train[0]

# Creating a model
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compiling model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training a model
model.fit(features_train, encoding_labels_train, epochs=300, batch_size=10)

# Evaluate the model
scores = model.evaluate(features_test, encoding_labels_test)
print("\nAccuracy: %.2f%%" % (scores[1]*100))

model.summary()

model.count_params()