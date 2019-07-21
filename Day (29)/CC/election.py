# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:51:58 2019

@author: Sahil
"""

"""
Q2. Code Challenge
code challenge - election data

1. Fetch the top parties of each state within each constituency with their vote %.

2. Visualize the top parties vote % in each constituency for Rajasthan.

3. Visualize the total seats gained by each party in each states.

4. Visualize the total seats won by the parties in the whole country
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("election.csv")

dataset.isnull().any(axis=0)  



#1

df2 = dataset[['Party','State','Constituency','%']]
df2_sorted= df2.sort_values( by='%', ascending = False)
df2_sorted = df2_sorted.drop_duplicates(subset = 'Constituency')

#2

df3 = dataset[dataset['State'] == 'Rajasthan'][['Party','Constituency','%']]
df3_sorted= df3.sort_values( by='%', ascending = False)
df3_sorted = df3_sorted.drop_duplicates(subset = 'Constituency')

df3_sorted.plot.bar()

# or use group and
#df3_sorted.plot.bar( x =  , y = )




#3

df4 = dataset[['Party','State','Constituency','%']]
df4_sorted= df4.sort_values( by='%', ascending = False)
df4_sorted = df4_sorted.drop_duplicates(subset = 'Constituency')

df4 = df4_sorted.groupby(['Party','State'])['Constituency'].count()
df4 = df4.head()
df4.plot.bar()



#4

df5 = dataset[['Party','State','Constituency','%']]
df5_sorted= df5.sort_values( by='%', ascending = False)
df5_sorted = df5_sorted.drop_duplicates(subset = 'Constituency')

df5 = df5_sorted.groupby(['Party'])['Constituency'].count()
#df5 = df5.head()
df5.plot.bar() 