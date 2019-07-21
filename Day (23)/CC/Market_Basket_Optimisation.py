# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:49:48 2019

@author: Sahil
"""
"""

Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.
"""

import pandas as pd
from apyori import apriori


"""
# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

transactions = []

for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
"""


transactions = []

file  = open('Market_Basket_Optimisation.csv')
for line in file:
    transactions.append(line.split(','))
    


# Training Apriori on the dataset
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

results = list(rules)




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



#2
#dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)



file  = open('Market_Basket_Optimisation.csv')
from collections import defaultdict
dict1 = defaultdict(int)


for line in file:
    list1 = line.split(',')
    for item in list1:
        dict1[item] += 1

import operator
sorted_dict1 = dict(sorted(dict1.items(), key=operator.itemgetter(1),reverse=True)[:11])
print(sorted_dict1)



        
        
        
   
     
        
        
        
        
        
        

"""
fp = open("Market_Basket_Optimisation.csv",'rt')
contents = fp.readlines()
print(contents)
"""




