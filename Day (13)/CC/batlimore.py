# -*- coding: utf-8 -*-
"""
Created on Thu May 23 05:46:18 2019

@author: Sahil
"""


"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
    
"""

import pandas as pd
import numpy as np
df = pd.read_csv("Baltimore_City_Employee_Salaries_FY2014.csv")

#2
group1 =df.groupby(['JobTitle'])['AnnualSalary']
group1.groups

agg = group1.agg([np.sum,np.mean,np.std,np.min,np.max])



sort_data = df.sort_values(['AnnualSalary'],ascending=0)
print("{} gets the highest salary {}".format(sort_data.iloc[0,0],sort_data.iloc[0,5]))


#3
group2 = df.groupby(['JobTitle'])
group2.groups
sorted(group2.groups.keys())


#4
employee_no = df['JobTitle'].value_counts()
employee_no[0:10].plot('bar')


#5
spends_most = agg.sort_values(['sum'],ascending=0)
print("{} spends the most {}".format(spends_most.index[0],spends_most.iloc[0,0]))

agg['sum'][0:10].plot('bar')

#6
agency = df[['AgencyID','Agency']]
print(agency)

#7

missing = df['GrossPay'].isnull()
print(missing)
missing.sum()