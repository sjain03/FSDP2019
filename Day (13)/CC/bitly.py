# -*- coding: utf-8 -*-
"""
Created on Fri May 24 06:37:23 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
    (usagov_bitly_data.json)
    In 2011, URL shortening service Bitly partnered with the US government website
    USA.gov to provide a feed of anonymous data gathered from users who shorten links
    ending with .gov or .mil. 
    In 2011, a live feed as well as hourly snapshots were available
    as downloadable text files. 
    This service is shut down at the time of this writing (2017),
    but we preserved one of the data files.
    In the case of the hourly snapshots, each line in each file contains a common form of
    web data known as JSON. (Use usagov_bitly_data.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

Hint:
    http://1usagov.measuredvoice.com/2011/
    
"""
import pandas as pd

import numpy as np


df = pd.read_json("usagov_bitly_data.json", lines =True)

df.isnull().any(axis=0)

df = df.replace(np.nan,"Missing")
df = df.replace(' ',"Unknown")


df_tz = df['tz'].value_counts().head(10)
print(df_tz)

df_tz_count = df['tz'].value_counts()
print(df_tz_count)

df_tz.plot.bar()


# Spiliting the Fetched series of browser info. according to tokens
tokens_df = df['a'].str.split(n=1, expand=True).add_prefix("Token_")

# Fetching the frequency of the browser capability
browser_cap_count = tokens_df['Token_0'].value_counts()

# Plotting bar graph for top 5 browser capability
browser_cap_count.head().plot.bar()

#Filling the missing values in the token parts with mising string
tokens_df = tokens_df.replace(np.nan, 'Mising')



# Initializing the os column as Not windows
tokens_df["os"] = 'Not Windows'

# Applying the conditions to find the windows os user and initializing their os column as Windows
tokens_df["os"][tokens_df["Token_1"].str.find("Windows") != -1] = "Windows"
