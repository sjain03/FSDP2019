# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:11:39 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""

A1 = int(input("Enter the marks of A1 >"))
A2 = int(input("Enter the marks of A2 >"))
A3 = int(input("Enter the marks of A3 >"))

E1 = int(input("Enter the marks of E1 >"))
E2 = int(input("Enter the marks of E2 >"))

weighted_score = ( A1 + A2 + A3 ) * 0.1 + (E1 + E2 ) * 0.35
print("weighted score is {}".format(weighted_score))

