# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:38:13 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""

from collections import OrderedDict

od = OrderedDict()

while True:
    user_input = input("Enter the item and price > ")
    
    if not user_input:
        break
    
    temp =user_input.split()
    price = temp[-1]
    
    item = " ".join(temp[0:2])     #item = " ".join(temp[0:2]) or item = " ".join(temp[:-1])
    
    od[item] = od.get(item,0) + int(price)
    
for k,v in od.items():               #items is a method
    print(k,v)






































"""
dict1 = {'BANANA FRIES':12,'POTATO CHIPS':30,'APPLE JUICE':10,'CANDY':5}

dict2 = {}
while True:
        item_name = input("Enter the item >")
        if not item_name:
            break
       
        quantity = int(input("Enter the no item >"))
        if not quantity:
            break
        
        dict2[item_name] = quantity
        print(dict2)
print (dict2.get(quantity))

        for i in item_name:
            if i in dict1.keys():
                a = a + quantity
                dict2[item_name] = quantity
        print(dict2)
"""  
                
                
    




