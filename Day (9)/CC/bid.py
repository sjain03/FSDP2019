# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:50:36 2019

@author: Sahil
"""

"""
Code Challenge 3
In the Bid plus Code Challenege

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database
"""


"""
https://www.db4free.net
https://www.db4free.net/phpMyAdmin/
MySQL Host Name : db4free.net
Port : 3306
MySQL database name:  yourdbname
MySQL username: yourusername
MySQL user password: dbpassword
Email address:  your emailid
MYSQL URL : mysql://yourusername:dbpassword@db4free.net/yourdbname

"""

"""
https://www.db4free.net/signup.php?language=en

"""


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
    #get_pdf = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    #get_pdf.click()
    A.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text)
    B.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text)
    C.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text)
    D.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text)
    E.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text)
    F.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text)




import mysql.connector
# connect to  MySQL server along with Database name

#conn = mysql.connector.connect(user='yourusername', password='dbpassword',host='db4free.net', database = 'yourdbname')
conn = mysql.connector.connect(user='yourusername', password='dbpassword',host='db4free.net', database = 'bid_db')

# creating cursor
c = conn.cursor()

#c.execute("DROP TABLE bids")

c.execute("""CREATE TABLE bids(
        bid_no TEXT,
        items TEXT,
        quantity_req INTEGER,
        dept TEXT,
        start_date TEXT,
        end_date TEXT
        )""")

for i in range(0,9):
    c.execute("INSERT INTO bids VALUES('"+A[i]+"' , '"+B[i]+"' , "+C[i]+" , '"+D[i]+"' , '"+E[i]+"' , '"+F[i]+"')")
                                        #string                   #integer



c.execute("SELECT * FROM bids")
print ( c.fetchall() )

conn.commit()
conn.close()
