# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:08:04 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""
def fix_teen(x):
    if(x==13 or x==14 or x== 17 or x==18 or x==19):
        return 0
    else:
        return x
    

dict1 = {}
while True:
    key = input("enter the key >")
    if not key:
        break
    value = input("enter the value>")
    if not value:
        break
    dict1[key] = value
print(dict1)

sum1=0

for x in dict1.values():
    y = fix_teen(int (x))
    sum1 = sum1 + y
print(sum1)
    
    
    
    