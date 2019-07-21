# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:01:34 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""



def Sum(arr):
  length = len(arr)
  total = 0

  if length==0:
    return 0

  for x in range(length):
    if arr[x]!=13:
      if arr[x-1]!=13:
        total= total + arr[x]

  return print(total)


list1 = []
for i in range(0,7):
    element = int(input("Enter the elements >"))
    list1.append(element)
print(list1)
    
Sum(list1)










"""

input_string = input("Enter a list element separated by space ")
list  = input_string.split()
print("Calculating sum of element of input list")
sum = 0
for num in list:
    sum += int (num)
    print("Sum = ",sum)
"""
"""
def sum13(nums):
  sum = 0
  pos = 0
  while pos < len(nums):
    if nums[pos] == 13:
      pos += 1
    else:
      sum += nums[pos]
    pos += 1
  return sum
"""