# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:13:17 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""
list1 = []
for i in range(0,4):
    element = int(input("Enter the elements >"))
    list1.append(element)
print(list1)




 
def Add(list1):
    sum = 0
    for x in list1:
        sum = sum + x
    return print(sum)


def Mul(list1):
    mul = 1
    for i in list1:
        mul = mul * i
    return print(mul)




def Largest(list1):
    list1.sort()
    largest = list1[-1]
    return print(largest)




def Smallest(list1):
    list1.sort()
    smallest = list1[0]
    return print(smallest)



def Remove_Duplicates(lst):
    n_lst = []
    for i in lst:
        if i not in n_lst:
            n_lst.append(i)
    return n_lst


def Sorted(lst):
    s = len(lst)
    us = True
    while us:
        us = False
        i = 0
        while i<s-1:
            if lst[i] > lst[i+1]:
                t = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = t
                us = True
            i += 1
    return lst

    
def Print():
    Add(list1)
    Mul(list1)
    Largest(list1)
    Smallest(list1)
    Remove_Duplicates(list1)
    Sorted(list1)
Print()
    

    




