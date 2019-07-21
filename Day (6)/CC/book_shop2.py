# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:23:20 2019

@author: Sahil
"""


"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of list with 
    [order number, total amount of order].
    
   Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
      
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
"""

orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

from collections import OrderedDict


dict1 = OrderedDict()


list1 = []

for i in orders:
        a = i[0]
        info = (i[1:])
        for j in info:
           list1.append([a, (j[1] * j[2]) ])
print(list1)


"""
for i in orders:
    a =i[0]
    for j in range(1,len(i)):
        b = i[j][1]*i[j][2]
    list1.append([a,b])
print(list1)
  """    
        
        
        
for new in list1:
        dict1[new[0]] = dict1.get(new[0], 0) +  new[1] 
print(dict1)



dir (OrderedDict)
help (OrderedDict.get)          











from functools import reduce

orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
	       [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
	       [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]



result = map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2] , x[1:])) , orders)

a  = list(result)
print(a)



#result2 = map(lambda x : ( [ x[0] , reduce (lambda y,z: y+z ,x[1:] ) ]) , a)


result2 = map(lambda x: [x[0]] + [reduce(lambda a,b: a + b, x[1:])], a)
b = list(result2)
print(b)


#result2 = list(map(lambda x: [x[0]] + [round(reduce(lambda a,b: a + b, x[1:]),2)], result))





