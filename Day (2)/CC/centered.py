# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:01:17 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""

    
list1 = []  
for i in range(0,5):
    element = int(input("Enter the element >"))
    list1.append(element)
print(list1)


def Centered(arr):
    total = 0
    items = len(arr)
   
    arr.sort()
    largest = arr[-1]
    smallest = arr[0]
    
    for x in arr:
        total = total + x
    average = (total - largest - smallest )// (items - 2)
    return print(average)
Centered(list1)   



"""
largest = max(arr)
smallest = min(arr)      
"""
    
    
    
    

