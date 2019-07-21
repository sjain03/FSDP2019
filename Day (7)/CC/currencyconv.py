# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:35:28 2019

@author: Sahil
"""


"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
"""
 http://free.currencyconverterapi.com
 
 https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=8b85a50042922af37f98
"""
import json
import requests

url1 = "http://free.currencyconverterapi.com/api/v5/convert"
url2 = "?q=USD_INR&compact=ultra"
url3 = "&apiKey=8b85a50042922af37f98"

url = url1 +url2 +url3

response =requests.get(url)
response.content

jsondata = response.json()

usd = int(input("enter the amount >"))
a = jsondata['USD_INR']

b = usd*a
print(b)
