# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:44:07 2019

@author: Sahil
"""

"""

Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 100(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
  User Input 
    Not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz  
"""

for i in range(1,100):
    if i%3==0 and i%5 == 0:
        print("Fizzbuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i%5 == 0:
        print("Buzz")
        continue
    print(i)
    