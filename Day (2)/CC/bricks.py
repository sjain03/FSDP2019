# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:30:24 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""

def Brick(small,big,goal):
    if goal % 5 > small:
        return print("False")
    else:
        c = small*1 + big*5
        if c >= goal:
            return print("True")
        else:
            return print("False")
       

str1 = str(input("Enter the string >"))
print(str1)
list1 = str1.split()
print(list1)

small = list1[0]

big = list1[1]

goal = list1[2]

Brick(small,big,goal)


"""
list1 = []
for i in range(0,5):
    ele = input("Enter element >")
    list1.append(ele)
print(list1)
"""


"""
list1 = list(inpu("Enter the List"))
print(list1)

"""