# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:28:57 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
str1 = str(input("Enter the string >"))                     #split:string -> list & join: list ->string
print(str1)
list1 = str.split(str1)
print(list1)

for i in list1:
    temp = i[::-1]
    if (i == temp ):
        print("True")
    else:
        print("False")
    
    





            
    
  """
  num = int(input("Enter number of elements in list: ")) 
  
# iterating till num to append elements in list 
for i in range(1, num + 1): 
    ele = int(input("Enter elements: ")) 
    list1.append(ele) 
    """
    
#list1 = list(str1)   
    
