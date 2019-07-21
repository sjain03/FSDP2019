# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:45:26 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""

str = "RESTART"

dir (str)
help (str.replace)

str.replace("R","$")

index = str.find("R")
str1 = str[0:index+1]
print(str1)

str2 = str[index+1:7]
print(str2)

str3 = str2.replace("R","$")

print(str1 + str3)

