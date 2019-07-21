# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:28:48 2019

@author: Sahil
"""
"""
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)

"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_table("Auto_mpg.txt", delim_whitespace= True, header = None ,names = ["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"] )




#2

max_value = dataset.sort_values(by ='mpg',ascending = 0)
car_name = max_value.iloc[0,8]
print("Car Name with highest miles per gallon value:", car_name )





#3

features = dataset.drop(['mpg','car name'], axis=1)  
labels = dataset['mpg']  




features['horsepower'] = features['horsepower'].replace("?",0.0)


"""
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features['car name'] = labelencoder.fit_transform(features['car name'])
"""



from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 


#Decision Tree

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(features_train,labels_train)


label_pred = regressor.predict(features_test)

df=pd.DataFrame({'Actual':labels_test, 'Predicted':label_pred})  
print(df)




#Random Forest

from sklearn.ensemble import RandomForestRegressor
regressor2 = RandomForestRegressor(n_estimators = 25 , random_state = 0 )
regressor2.fit(features_train,labels_train)


labels_pred2= regressor2.predict(features_test)
df2 = pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred2})
print(df2)


#4

x= [6,215,100,2630,22.2,80,3]
x = np.array(x)
x = x.reshape(1,-1)

#random Forest
label_pred3 = regressor2.predict(x)
print(label_pred3)





"""
#decision tree
label_pred4 = regressor.predict(x)
print(label_pred4)
"""