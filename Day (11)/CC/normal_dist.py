# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:01:31 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""

import numpy as np
values = np.random.normal(150,20,1000)
print(values)


import matplotlib.pyplot as plt

plt.hist(values, 50)
plt.show()


sd = np.std(values)

print("Standard Deviation is: ", sd)
print("Variance is: ",sd**2 )