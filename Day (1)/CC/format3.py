# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:42:57 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format3.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    W*e*l*c*o*m*e* *t*o* *P*i*n*k* *C*i*t*y* *J*a*i*p*u*r
"""
str1 = input("Enter the string >")
print(str1)

dir(str)
help (str.join)

"*".join(str1)