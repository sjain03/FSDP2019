# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:31:49 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""

import numpy as np
from collections import Counter

random = np.random.randint(5,15,40)
#print(random)

f_counter = Counter( random )

# Getting the most frequent value from the list of tuples of all the values
most_frequent_value = f_counter.most_common()[0][0]

print ( "The most Frequent Number is",most_frequent_value )



#using mode
from scipy import stats
mode = stats.mode(random)
#print("Mode value is: ", stats.mode(x)[0])
print(mode)