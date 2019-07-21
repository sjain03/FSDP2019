# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:36:52 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. ( SyLvEsTeR )
"""
dir (str)
help (str.title)

str = "Jupyter NoteBook"
print(str.lower())
print(str.upper())
print(str.title())