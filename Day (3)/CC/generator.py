# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:12:58 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""
str1 = input("Enter the elements >")
list1 = list(str1)
print(list1)

while ',' in list1:
    list1.remove(',')
print(list1)

tuple1 = tuple(list1)
print(tuple1)

"""
import ast
str1 = "{"ele":2}"
"""