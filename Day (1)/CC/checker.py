# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:27:38 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Name Printing Checkerboard pattern
  Filename: 
    checker.py
  Problem Statement:
    Print the checkerboard pattern using escape Codes and Unicode 
    with multiple print statements and the multiplication operator 
  Hint: 
    Eight characters sequence in a line and 
    the next line should start with a space
    try to use the * operator for printing
  Input:
    No input required
  Output:
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *

"""
i = 0
while(i<4):
    print("* "*8)
    if(i==3):
        break
    print(" *"*8)
    i=i+1
