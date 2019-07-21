# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:53:42 2019

@author: Sahil
"""

"""

Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
    yogendra_54@forsk.com
  Output:
    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]

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
        
        
     

    