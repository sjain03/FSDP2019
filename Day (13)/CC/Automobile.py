# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:28:22 2019

@author: Sahil
"""


"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""

import pandas as pd

df = pd.read_csv("Automobile.csv")


df_make = df['make'].value_counts()



import matplotlib.pyplot as plt

explode = (0.3,0,0,0,0,0,0,0,0,0,0)

plt.pie(df_make.values[0:11],explode = explode, labels =df_make.index[0:11],autopct='%2.2f%%' )




plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
