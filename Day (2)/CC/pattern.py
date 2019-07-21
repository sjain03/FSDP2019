# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:07:51 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""
i = int(input("enter the no of rows >"))
for i in range(0,i+1):
    print("*"*i)
for i in range(i-1,0,-1):
    print ("*"*i)

"""
j = i-1
while j > 0:
    print("*"*j)
    j = j-1
"""
