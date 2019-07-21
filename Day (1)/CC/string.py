# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:16:56 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    String Handling
  Filename: 
    string.py
  Problem Statement:
    Take first and last name in single command from the user and print  
    them in reverse order with a space between them, 
    find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester 
"""
str1 = input("Enter the firstname >")
print(str1)
str2 = input("Enter the lastname >")
print(str2)
str3 = (str2 + " " + str1)
print(str3)

str3.find('s')

str3.index('n')

print(str3[0:10])

