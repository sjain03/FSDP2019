# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:39:49 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

def translate(s):
    consonant = "bcdfghjklmnpqrstvwxyz"
    r = ""
    for i in s:
        r = r +i
        if i in consonant:
            r = r + "o" + i
    return print(r)

str1 = input("Enter the String >" )
translate(str1)


