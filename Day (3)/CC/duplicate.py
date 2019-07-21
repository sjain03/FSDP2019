# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:09:49 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""

list1 = [12,24,35,24,88,120,155,88,120,155]
set1 = set(list1)
list2 = list(set1)
print(list2[::-1])
