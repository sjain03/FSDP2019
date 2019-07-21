# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:15:21 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""
def Pangram(str1): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str1.lower(): 
            return print("NOT PANGRAM")
    
    return print("PANGRAM")

str1 = input("Enter the String >")
Pangram(str1)
