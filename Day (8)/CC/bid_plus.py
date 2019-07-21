# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:27:46 2019

@author: Sahil
"""

"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""


"""
#bid
//*[@id="pagi_content"]/div[1]/div[1]/p[1]/a
//*[@id="pagi_content"]/div[2]/div[1]/p[1]/a
//*[@id="pagi_content"]/div[3]/div[1]/p[1]/a

#items
//*[@id="pagi_content"]/div[1]/div[2]/p[1]
//*[@id="pagi_content"]/div[2]/div[2]/p[1]
//*[@id="pagi_content"]/div[3]/div[2]/p[1]

#quantity
//*[@id="pagi_content"]/div[1]/div[2]/p[2]/span
//*[@id="pagi_content"]/div[2]/div[2]/p[2]/span


#dept
//*[@id="pagi_content"]/div[1]/div[3]/p[2]
//*[@id="pagi_content"]/div[2]/div[3]/p[2]
//*[@id="pagi_content"]/div[3]/div[3]/p[2]

#start date
//*[@id="pagi_content"]/div[1]/div[4]/p[1]/span
//*[@id="pagi_content"]/div[2]/div[4]/p[1]/span

#end date
//*[@id="pagi_content"]/div[1]/div[4]/p[2]/span
//*[@id="pagi_content"]/div[2]/div[4]/p[2]/span


xpath is common
.
.
.
.
"""

import pandas as pd
from selenium import webdriver
 
source  = "https://bidplus.gem.gov.in/bidlists"

driver = webdriver.Firefox(executable_path=r'G:/geckodriver.exe')
driver.get(source)



A=[]
B=[]
C=[]
D=[]
E=[]
F=[]



for i in range(1,10):
    #download pdf
    get_pdf = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    get_pdf.click()
    A.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text)
    B.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text)
    C.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text)
    D.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text)
    E.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text)
    F.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text)





import pandas as pd
from collections import OrderedDict

col_name= ["Bid No","Items","Quantity Req","Department","Start Date","End Date"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))
df = pd.DataFrame(col_data)
df.to_csv("bid.csv")
