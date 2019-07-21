# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:00:25 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
"""    
kilometre = float(input("Enter the Kilometres >"))
print(kilometre)
cost = 80
average = 18
cost_perday = float((kilometre/average)*cost)
print(cost_perday)