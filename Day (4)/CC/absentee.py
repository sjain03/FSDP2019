# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:53:14 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

fp = open("absentee.txt","wt")

with open("absentee.txt","wt") as fp:
    for name in range(0,25):
        name = input("Enter the name >")
        fp.write(name+"\n")
        if not name:
            break
    
fp = open("absentee.txt","rt")
line = fp.readlines()
print(line)
        