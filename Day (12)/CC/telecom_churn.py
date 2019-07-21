# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:22:28 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    
"""
"""
File Name : Telecom_Churn.py
problem Statement:
To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght? Predict and print it
6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
7. In which area code the international plan is most availed?
"""

import pandas as pd

df = pd.read_csv("Telecom_churn.csv")

#filter
#1
df_sub= df[(df['churn'] == True) & \
           
           (df['international plan'] == 'yes') & \
           
           (df['voice mail plan'] == 'yes' )
           
           ]

inter_and_voice  = df_sub['international plan'].value_counts()
print("No. of churned customer in international plan :", inter_and_voice)

#2
df_churned_charges = df[df['churn'] == True ] [['total intl charge']]

df_nonchurned_charges = df[df['churn'] == False ] [['total intl charge']]

total_churned_charges = df_churned_charges.sum()
print(total_churned_charges)

total_nonchurned_charges = df_nonchurned_charges.sum()
print(total_nonchurned_charges)

#df_churned_charges.hist(bins=20,grid=False)
#df_nonchurned_charges.hist(bins=20,grid=False)


import matplotlib.pyplot as plt
labels = 'churned_charges', 'nonchurned_charges'
sizes = [total_churned_charges[0],total_nonchurned_charges[0] ]
colors = ['gold', 'blue']
explode = (0.1, 0)  # explode 1st slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)





#3
df_night_calls= df[(df['churn'] == True)].sort_values('total night calls')

#df_night_calls['total night calls'].max()

highest_night_calls = df_night_calls[df_night_calls['total night calls'] == df_night_calls['total night calls'].max()]
print(highest_night_calls['state'])




df_churned = df[df['churn'] == True ] [['total day calls', 'total eve calls', 'total night calls']]


import matplotlib.pyplot as plt
labels = 'day_calls', 'eve_calls', 'night calls'
sizes = [df_churned['total day calls'],df_churned['total eve calls'],df_churned['total night calls'] ]
colors = ['gold', 'blue','green']
explode = (0.1, 0,0)  # explode 1st slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)



#4
churned_df = df[df['churn'] == True]
 
call_analysis = churned_df.iloc[:, 7:19].sum().sort_index()
visual_2 = call_analysis.plot.bar()





#5
df_account_length= df.sort_values('account length')

maximum_account_length = df_account_length[df_account_length['account length'] == df_account_length['account length'].max()]
print(maximum_account_length)


#6
customer_care = df[df['churn'] == True][['customer service calls']]
cc_counts = customer_care['customer service calls'].value_counts()
print(cc_counts)


#7

df_international_plan = df[df['international plan'] == 'yes' ]
max = df_international_plan['area code'].value_counts()


print("The area code {} has the maximum {} international plans".format(max.index[0],max.values[0]))