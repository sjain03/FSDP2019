# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:58:57 2019

@author: Sahil
"""
"""

Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("iq_size.csv")

features = dataset.iloc[:,1:].values
labels = dataset.iloc[:, 0].values


#1 linear regression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features, labels)

label_pred = regressor.predict(features)
print (label_pred)


x=[90,70,150]

x = np.array(x).reshape(1,-1)
iq_pred = regressor.predict(x)
print(iq_pred)




#optimal model using Backward elimination
import statsmodels.api as sm

#adds a constant column to input data set.
features = sm.add_constant(features)



features_opt = features[:, [0, 1, 2, 3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [1 , 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()



print (" Brain Size is more useful in predicting intelligence.")






















"""
#quadratic

from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 2)
features_poly = poly_object.fit_transform(features)

from sklearn.linear_model import LinearRegression
reg2 = LinearRegression()
reg2.fit(features_poly, labels)


x=[90,70,150]
x = np.array(x).reshape(1,-1)
iq_pred2 = reg2.predict(poly_object.transform(x))
print(iq_pred2)
"""


