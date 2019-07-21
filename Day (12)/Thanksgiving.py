# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:11:49 2019

@author: Sahil
"""


"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
  Hint:

"""


import pandas as pd
import numpy as np

#loading dataset
df = pd.read_csv("thanksgiving.csv",encoding ='Windows 1252')

#names of columns
columns_name = list(df.columns)

#converting the column name to single word names
col_name = [x for x in range(0, 65)]

df.columns = col_name

#data for people who celebrate thanksgiving
df = df[df[1] == "Yes"]


#repalcing nan with Missing
df = df.replace(np.nan, 'Mising')


# regional and income-based patterns in what Americans eat for Thanksgiving dinner

region_based = df.groupby(64)[2].value_counts().unstack()
region_based.fillna(0)

income_based = df.groupby(63)[2].value_counts().unstack()
income_based.fillna(0)


# Using the apply method to Gender column to convert Male & Female
def Gender(x):
    if x == 'Male':
        x = 'M'
    elif x == 'Female':
        x = 'F'
    else:
        pass
    return x
    
df[62] = df[62].apply(Gender)
        

"""
#Using the apply method to clean up income
df[63] = df[63].replace(['Prefer not to answer', 'mising'],['0','0'] )


def Income(x):
   """
