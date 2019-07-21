# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:27:35 2019

@author: Sahil
"""

"""
Hands On 1
"""
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list

list1 = []
for num in range(1,21):
    list1.append(num)
print(list1)

print(list1[1:20:2])
print(list1[0:20:2])

"""
Hands On 2
"""
# Make a function to find whether a year is a leap year or no, return True or False 

def leapyear(y):
    if(y%4 == 0):
        return print(" is Leap Year")
    elif(y%400 == 0):
        return print("is Leap Year")
    elif(y%100 == 0):
        return print("is not a leap Year")
    else:
        return print("is not a leap year")
    
a = int(input("enter the year >"))
leapyear(a)

 


"""
Hands On 3
"""
# Make a function days_in_month to return the number of days in a specific month of a year

def days_in_month(a):
    if (a == "jan" or a == "march" or a =="may" or a == "july" or a =="august" or a =="oct" or a =="dec"):
        return print("31 days")
    elif ( a == "feb"):
        return print("28 Days")
    else:
         return print("30Days")
     
m = str(input("enter the month >"))
days_in_month(m)




"""
list1 = ['jan','feb']
list2 = [31, 28]   
list3 = zip(list1,list2) 
"""

