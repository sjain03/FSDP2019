# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:01:03 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Sorting
  Filename: 
    sorting.py
  Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score
  Input: 
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
  Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
"""


student_list = []

while True:
    user_input = input("Enter Name, Age and Score: ")
    
    if not user_input:
        break
    
    name, age, marks = user_input.split(",")
    
    student_list.append( (name, int(age), int(marks) ) )

student_list.sort()
print (student_list)



















"""
import operator
list2 =[]
for i in range(0,5):
    str1 = input("Enter the values >")
    list1= str.split(str1)
    tuple1= tuple(list1)
    print(tuple1)
    list2.append(tuple1)
    print(list2)
    
    
list2.sort(key = operator.itemgetter(0,1,2))
print(list2)

dir (operator)
help (operator.itemgetter)
"""




