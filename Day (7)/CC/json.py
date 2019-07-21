# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:03:10 2019

@author: Sahil
"""


"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
"""
openweathermap.org
jkg031098@gmail.com
123456789

api id:
api :
"""



import requests
#city=input("enter city")
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=jaipur"
url3 = "&appid=74b6a61b433f172af7ffef082940266d"

url = url1 + url2 + url3
print (url)

response = requests.get(url)
response.content

jsondata=response.json()

# Since we know that the content type is json we can call the json() function to get the data converted to python data type (dict)
a =jsondata["coord"]   
b=jsondata["main"]["temp"]
c=jsondata["weather"][0]["main"]
d=jsondata["main"]
e=jsondata["wind"]["speed"]
f=jsondata["sys"]["sunrise"]
g=jsondata["sys"]["sunset"]

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
