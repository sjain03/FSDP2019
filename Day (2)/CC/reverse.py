# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:23:13 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""

def reverse(s):
    a = s[::-1]
    return print(a)

str1 = input("Enter the String >")
reverse(str1)










""""
def reverse(s): 
  str1 = "" 
  for i in s: 
    str1 = i + str1
  return print(str1)
  
str1 = input("Enter the String >")
reverse(str1)
"""