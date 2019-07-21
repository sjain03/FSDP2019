# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:24:38 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels ="AEIOUaeiou"
list1 = []
temp=[]
for item in state_name:
    if len(temp)>0:        #empty temp again as it will contain characters from previous item
        temp=[]
    for i in item:
        if i not in vowels:
            temp.append(i)
    list1.append("".join(temp))             
print (list1)







"""
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels = ['a','e','i','o','u']




list1 = list(state_name[0])
print(list1)

for vowels in list1:
    list1.remove(vowels)
print(list1)
temp1 ="".join(list1)
print(temp1)






list2 = list(state_name[1])
print(list2)

for vowels in list2:
    list2.remove(vowels)
print(list2)
temp2 ="".join(list2)
print(temp2)





list3 = list(state_name[2])
print(list3)

for vowels in list3:
    list3.remove(vowels)
print(list3)
temp3 ="".join(list3)
print(temp3)




list4 = list(state_name[3])
print(list4)

for vowels in list4:
    list4.remove(vowels)
print(list4)
temp4 ="".join(list4)
print(temp4)


"""

"""

vowels = "aeiou"


name = "Sahil"
name = name.lower()
list1 = []

for char in name:
    if char not in vowels:
        list1.append(char)
print ("".join(list1))
"""









