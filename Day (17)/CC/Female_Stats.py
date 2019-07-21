# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:30:43 2019

@author: Sahil
"""
"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Female_Stats.csv")

features = dataset.iloc[:, 1:3].values
labels = dataset.iloc[:, 0].values



#1  Building the optimal model using Backward Elimination
import statsmodels.api as sm

features = sm.add_constant(features)


features_opt =features[:,[0,1,2]]

regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()






#2 When Father’s Height Is Held Constant

features2 = dataset.iloc[:, [1,2]].values
features2[:,0] = features2[:,0]+1 



import statsmodels.api as sm

features2 = sm.add_constant(features2)
regressor_OLS2 = sm.OLS(endog = labels, exog = features2).fit()
regressor_OLS2.summary()


print("When Father's Height is Held Constant then the average height increase by",regressor_OLS2.params[1])

#3 When Mother’s Height Is Held Constant

features3 = dataset.iloc[:, [1,2]].values
features3[:,1] = features2[:,1]+1 



import statsmodels.api as sm

features3 = sm.add_constant(features3)
regressor_OLS3 = sm.OLS(endog = labels, exog = features3).fit()
regressor_OLS3.summary()        #check const


print("When Mother's Height is Held Constant then the average height increase by",regressor_OLS3.params[2])
































"""
Another Way


#model train3
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features, labels)

aveg = labels.mean()




#2

features2 = dataset.iloc[:, [1,2]].values
features2[:,0] = features2[:,0]+1 


pred2 = lin_reg.predict(features2)

aveg2 = pred2.mean()





#3


features3 = dataset.iloc[:, [1,2]].values
features3[:,1] = features2[:,1]+1 


pred3 = lin_reg.predict(features3)

aveg3 = pred3.mean()
"""




#labels.shape
#labels =labels.reshape(-1,2)
