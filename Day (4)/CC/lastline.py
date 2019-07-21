# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:34:24 2019

@author: Sahil
"""


"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""
x = input("Enter the name of file")
fp = open(x,"rt")

last_line = fp.readlines()[-1]
print(last_line)

fp.close()
