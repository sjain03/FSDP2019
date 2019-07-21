# -*- coding: utf-8 -*-
"""
Created on Mon May 20 06:33:04 2019

@author: Sahil
"""
"""

Fortune Teller (Horoscope)

A program that checks your horoscope on various astrology sites and puts them 
together for you each day. The code should share the Horoscope on Twitter account
 of the user.
"""


from bs4 import BeautifulSoup
import requests
sunsign = input("Enter your sunsign >")
source = requests.get("https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/"+sunsign+"/").text


soup = BeautifulSoup(source,'lxml')

horoscope = soup.find('p',class_='margin-top-xs-0')
print(horoscope)

