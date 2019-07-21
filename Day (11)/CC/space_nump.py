# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:23:29 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""

str1 = input("Enter space seprated values >")
list1 = str1.split()
print(list1)

list2 =[]
for i in list1:
    list2.append(int(i))

import numpy as np

x = np.array(list2)

x = x.reshape(3,3)

print(x)

