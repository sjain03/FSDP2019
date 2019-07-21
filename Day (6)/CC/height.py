# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:17:09 2019

@author: Sahil
"""

"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""
from functools import reduce
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

people_filter = list(filter(lambda x: 'height' in x,people))

height = list(map(lambda x: x['height'],people_filter))



people_reduce = reduce(lambda x,y:x+y , height)

average = people_reduce/len(height)
print(average)

 


































from functools import reduce

def add(x,y):
    return x+y

print (reduce ( add, [2,18,9,22,17,24,8,12,27]) )







