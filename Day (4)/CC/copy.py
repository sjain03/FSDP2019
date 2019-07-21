# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:41:54 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

fp = open("words.txt","rt")
a = fp.read()
print(a)
fp.close()


fp1 = open("new1.txt","wt")
b = fp1.write(a)
fp1.close()
