# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:11:34 2019

@author: Sahil
"""

"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("kc_house_data.csv")
dataset = dataset.replace(np.nan,dataset.mean())


features = dataset.iloc[:,3:21].values
labels = dataset.iloc[:,2].values


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  


#Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)



# Linear Regression
#model train
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train)  


labels_pred = regressor.predict(features_test) 
#print(labels_pred)



from sklearn import metrics  
 
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, labels_pred))) 


print (np.mean(dataset.values[:,2]))



# Lasso & Ridge

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

ridge = Ridge()
lasso = Lasso()

ridge.fit(features_train, labels_train)  
lasso.fit(features_train, labels_train)  

predict_lasso = lasso.predict (features_test) 
predict_ridge = ridge.predict (features_test)


#score
print ("RSquare Value for Simple Regresssion TEST data is-") 
print (np.round (regressor.score(features_test,labels_test)*100,2))

print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lasso.score(features_test,labels_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (ridge.score(features_test,labels_test)*100,2))
