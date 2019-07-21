# -*- coding: utf-8 -*-
"""
Created on Fri May 10 19:04:57 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""
x = input("enter the name of file >")
fp  = open(x,"rt")
#print(fp.read())



#no. of lines
num_lines = 0
for line in fp:
    num_lines = num_lines + 1
print(num_lines)




fp.seek(0,0)
#no. of chars
num_char=0
for line in fp:
    list1 = line.split()
    for word in line:
        list2 = word.split(" ")
        num_char = num_char + len(list2)
print(num_char)


fp.seek(0,0)
#no. of words
num_words = 0
for line in fp:
    list1 = line.split()
    num_words = num_words + len(list1)
print(num_words)











fp.seek(0,0)
#no.of unique words
num_uwords = 0
unique_words =set()
for line in fp:
    list1 = line.split()
    #print(set(list1))
    #unq_words = set(list1)
    unique_words.update(list1)
print(unique_words)    


num_uwords = num_uwords + len(unique_words)
print(num_uwords)




"""
 
filename = input("Enter a filename: ")
 
number_of_characters = 0
number_of_words = 0
unique_words = set()
 
for number_of_lines, line in enumerate(open(filename), 1):
    number_of_characters += len(line)
    number_of_words += len(line.split())
    unique_words.update(line.split())
 
print("Number of lines: {}".format(number_of_lines))
print("Number of characters: {}".format(number_of_characters))
print("Number of words: {}".format(number_of_words))
print("Number of unique words: {}".format(len(unique_words)))
 """