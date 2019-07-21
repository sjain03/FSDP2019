# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:46:00 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""

import pandas as pd

df = pd.read_csv("Automobile.csv")

df.info()

df[df.isnull().any(axis=1)]

new_df = df.fillna(0)


#new_df = df['prices'].fillna(0)
#df[new_df.isnull().any(axis=1)]

#df_prices = new_df[['price']]         series
df_prices = new_df[['price']]          #dataframe

#numpyrepresentation of the data
df_prices.values 



print("Maximum :" ,df_prices.max() )


print("Minimum :" ,df_prices.min() )


print("Mean :" ,df_prices.mean() )


print("Median :" ,df_prices.median() )

print("Std :" ,df_prices.std() )


