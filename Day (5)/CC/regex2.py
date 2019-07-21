# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:10:54 2019

@author: Sahil
"""


"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""
import re
list1 =[]
while True:
    email = input("Enter the Email >")
    
    if not email:
        break
    list1.append(email)
    
list2 = []
for val in list1:
    if re.match(r'[a-z0-9-_]+@[a-z0-9]+\.[a-z]{2,4}',val):
        list2.append(val)

print(sorted(list2))
    