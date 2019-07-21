# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:48:07 2019

@author: Sahil
"""

"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""
import pandas as pd


dataset = pd.read_csv("Bahubali2_vs_Dangal.csv")

features = dataset.iloc[:, :-2].values  
label1 = dataset.iloc[:, 1].values 
label2 = dataset.iloc[:, 2].values 


from sklearn.linear_model import LinearRegression 
 
regressor1 = LinearRegression()  
regressor1.fit(features, label1) 

 
regressor2 = LinearRegression()  
regressor2.fit(features, label2) 

print("reg1 :", regressor1.intercept_)  
print ("reg1 :", regressor1.coef_)


print("reg2 :", regressor2.intercept_)  
print ("reg2 :", regressor2.coef_)


#regressor1.predict([10])
Bahubali = regressor1.coef_*10 + regressor1.intercept_
print ("Prediction_Bahubali2:", Bahubali)


#regressor2.predict([10])
Dangal  = regressor2.coef_*10 + regressor2.intercept_
print ("Prediction_Dangal:", Dangal )


if Bahubali > Dangal:
    print("Bahubali collects more on 10th day ")

else:
    print("Dangal collects more on 10th day")

#print (regressor1.predict(10))