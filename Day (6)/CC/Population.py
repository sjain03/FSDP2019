# -*- coding: utf-8 -*-
"""
Created on Mon May 13 19:06:37 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Population Counting
  Filename: 
    Population.py
  Problem Statement:
      
      The given input has a number of rows, each with four fields from a table, containing:

          Rank,City,Population,State or union territory
          1,Mumbai,"12,442,373",Maharashtra


    You are required to output:

        Country, State, Population of the state (obtained by summing up the population of each city in that state)  


    Sample Input

    1,Mumbai,"12,442,373",Maharashtra
    9,Pune,"3,124,458",Maharashtra
    13,Nagpur,"2,405,665",Maharashtra
    6,Chennai,"4,646,732",Tamil Nadu
    59,Salem,"831,038",Tamil Nadu


    Sample Output

    {"key":"India,Tamil Nadu","value":5477770}
    {"key":"India,Maharashtra","value":17972496}


    Explanation

    The population of India,Tamil Nadu is obtained by adding the population of 
    Chennai and Salem. 
    This process is repeated for India,Maharashtra and India,Maharashtra. 


    Refer to population.csv


"""

import csv

from collections import defaultdict

csv_file =  open("population.csv")

csv_reader = csv.reader(csv_file,delimiter=',')
next(csv_reader)
csv_list = list(csv_reader)

freq = defaultdict(int)

for item in csv_list:
    k = "India, " + item[-1]
    freq[k] += int(item[2].replace(',',''))      

print(freq)