# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:40:27 2019

@author: Sahil
"""
"""
Code Challenge 01: (Prostate Dataset)

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.
(a) Train the unregularized model (linear regressor) and calculate the mean squared error.
(b) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

"""
import pandas as pd
import numpy as np

dataset =pd.read_csv("Prostate_Cancer.csv")
dataset = dataset.replace(np.nan,dataset.mean())


features = dataset.iloc[:,2:10].values
labels = dataset.iloc[:,1].values

labels = labels.reshape(-1,1)



"""
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels[:,0] = labelencoder.fit_transform(labels[:,0])
#labels = labelencoder.fit_transform(labels)

labels =labels.astype(int)
"""

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  



from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)



# unregularized model
#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train)  



labels_pred = regressor.predict(features_test) 
print(labels_pred)



from sklearn import metrics  
 
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, labels_pred))) 


#print (np.mean(dataset.values[:,8]))




# regularized model

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

ridge = Ridge()
lasso = Lasso()

ridge.fit(features_train, labels_train)  
lasso.fit(features_train, labels_train)  

predict_lasso = lasso.predict (features_test) 
predict_ridge = ridge.predict (features_test)


from sklearn import metrics  
print('Lasso Mean Squared Error:', np.round(metrics.mean_squared_error(labels_test, predict_lasso),2)) 
print('Ridge Mean Squared Error:', np.round(metrics.mean_squared_error(labels_test, predict_ridge),2))
