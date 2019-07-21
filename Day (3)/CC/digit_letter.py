# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:47:19 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""

str1 = input("Enter the string >")
print(str1)
str2 = "abcdefghijklmnopqrstuvwxyz"
str3 = "0123456789"
letters = 0
digits = 0
for item in str1:
    if item in str2:
        digits = digits + 1
    if item in str3:
        letters = letters +1
print("Digits >",digits)
print("Letters >",letters)