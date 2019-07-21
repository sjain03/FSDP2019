# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:39:23 2019

@author: Sahil
"""


"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""
fp = open("romeo.txt","rt")

dict1 = {}
for line in fp:
    list1 = line.split()

    for i in list1:
        if i in dict1.keys():
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] =  1

print(dict1)









  
