# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:19:33 2019

@author: Sahil
"""


"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
"""

import pandas as pd
from apyori import apriori


# Data Preprocessing
dataset = pd.read_csv('BreadBasket_DMS.csv')
dataset = dataset.iloc[:,2:]

items_count = dataset['Item'].value_counts()

top_15 = items_count.iloc[0:15]
#or use head

#top_15 = items_count.iloc[0:15].plot.pie()


#1
import matplotlib.pyplot as plt

labels = top_15.index
sizes = top_15.values


plt.pie(sizes,  labels=labels,  autopct='%1.1f%%', startangle=0)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()




#2



transactions = []
def func1(arg): 
    transactions.append(list(set(arg)))            #set used not to repeat items in cookies
    
    
     
dataset2= dataset.groupby('Transaction')['Item'].apply(func1)

#dataset2= dataset.groupby('Transaction')['Item'].sum()


rules = apriori(transactions, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

results = list(rules)


#2


for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")