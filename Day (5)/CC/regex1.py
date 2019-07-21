# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:42:50 2019

@author: Sahil
"""

"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""
    


import re

N = input("Enter the string >")
print(N)
N1=  N.split()
print(N1)

for val in N1:
    if re.findall(r'[+-.]?[0-9]+\.[0-9]+',val):
        print('TRUE')
    else:
        print('FALSE')





