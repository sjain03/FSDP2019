# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:48:31 2019

@author: Sahil
"""
"""
Code Challenge
  Name: 
    Gas Mileage Calculator
  Filename: 
    mileage_cal.py
  Problem Statement:
    Assume my car travels 100 Kilometres after putting 5 litres of fuel. 
    Calculate the average of my car. 
  Hint: 
    Divide kilmeters by the litres used to get the average
"""
kilometre = float(input("Enter the Kilometres >"))
print (kilometre)
fuel = int(input("Enter the amount of fuel >"))
print (fuel)
avg = float(kilometre) / fuel
print (avg)