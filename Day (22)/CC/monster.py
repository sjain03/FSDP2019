# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:33:03 2019

@author: Sahil
"""


"""
Q.
Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, zip code is given, deal with it?
 
 Seperate the salary column on hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with their average
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
 """
 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset (Bivariate Data Set with 3 Clusters)
dataset = pd.read_csv('monster_com-job_sample.csv')

#checking null values
dataset.isnull().any(axis=0)

dataset = dataset.drop('date_added',axis=1)

new_df = dataset.dropna()


import re

re.findall(r'\,+[0-9]*',)


"""
dataset['salary'] = dataset['salary'].dropna()
"""


"""
#remove row that contains any nan
dataset2 = dataset.copy().dropna(how='any')
dataset2.shape
dataset2.isnull().any(axis=0)
"""


