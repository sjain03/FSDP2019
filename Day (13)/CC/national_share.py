# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:42:27 2019

@author: Sahil
"""

"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""
from bs4 import BeautifulSoup
import pandas as pd
import requests

link = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source = requests.get(link).text
soup = BeautifulSoup(source,'lxml')


right_table = soup.find('table',class_="wikitable")
print(right_table)

A = []
B = []


for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells)== 7:
        A.append(cells[1].text.strip())
        B.append(cells[4].text.strip())
    
df = pd.DataFrame()
df["State"] = A
df["National Share"]= B

#df_national_share= df.sort_values('National Share')       maximum

import matplotlib.pyplot as plt
explode = (0.5,0,0,0,0,0)

plt.pie(df.iloc[0:6,1], explode = explode, labels=df.iloc[0:6,0], autopct='%2.2f%%')



plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
