# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:26:56 2019

@author: Sahil
"""
"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


"""

from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text

soup = BeautifulSoup(source,"lxml")

print(soup)

right_table = soup.find("table",class_="table")
                        #tagname
A =[]
B=[]
C=[]
D=[]
E=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells)== 5:               #skip first row it contains 6 th 
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())



import sqlite3

conn = sqlite3.connect ( 'icc_rank.db' )

# creating cursor
c = conn.cursor()

#c.execute("DROP TABLE points_table")

c.execute("""CREATE TABLE points_table(
        Rank INTEGER,
        Team TEXT,
        Matches INTEGER,
        Points INTEGER,
        rating INTEGER
        )""")

for i in range(0,16):
    c.execute("INSERT INTO points_table VALUES('"+A[i]+"' , '"+B[i]+"' , '"+C[i]+"' ,' "+D[i]+"' , '"+E[i]+"')")
                                                #string      #string        #string      #string     #string



c.execute("SELECT * FROM points_table")
print ( c.fetchall() )


