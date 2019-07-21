# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:31:38 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""

dir(str)
help (str.join)
#"*".join(['Welcome','to','Pink','City','Jaipur'])

str = input("Enter the String >")
print(str.replace(" ","*"))







"""

list1 = []
for i in range(0,5):
    ele = input("Enter element >")
    list1.append(ele)
print(list1)

"*".join(list1)
"""
