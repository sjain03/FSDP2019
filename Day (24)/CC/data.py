# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:14:40 2019

@author: Sahil
"""

"""Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("data.csv")

dataset.isnull().any(axis=0)    #check null colums

dataset = dataset.copy().dropna(how='all',axis = 1)              #drop all nan columns

#1

#make seprate dataframes

country = dataset['Country']
country = country.dropna()                      #remove nan values
country_count = country.value_counts()

#country_count.plot.pie()

labels = country_count.index
sizes = country_count.values

plt.pie(sizes,  labels=labels,  autopct='%1.1f%%', startangle=0)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()




#2

#make seprate dataframes
Classification = dataset['Classification']
Classification = Classification.dropna()                      #remove nan values
Classification_count = Classification.value_counts()

top_2_Classification = Classification_count.iloc[0:2]
top_2_Classification.plot.bar()




#3

Artist = dataset['Artist Display Name']
Artist = Artist.dropna()                      #remove nan values
Artist_count = Artist.value_counts()

#Artist_count = Artist.value_counts().iloc[0:5]

labels = Artist_count.index
sizes = Artist_count.values

plt.pie(sizes,  labels=labels,  autopct='%1.1f%%', startangle=0)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()




#4

#make seprate dataframes
Culture = dataset['Culture']
Culture = Culture.dropna()                      #remove nan values
Culture_count = Culture.value_counts()

top_2_Culture = Culture_count.iloc[0:2]
top_2_Culture.plot.bar()
