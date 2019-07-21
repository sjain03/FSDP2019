# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:23:18 2019

@author: Sahil
"""



"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""

user_input = input("Enter the values >")
list1 = user_input.split()
print(list1)
if all([int(i)>0 for i in list1]) and any([i == i[::-1] for i in list1]):
    print("True")
else:
    print("False")
