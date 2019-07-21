
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:54:32 2019

@author: Sahil
"""

"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""
import sqlite3

conn = sqlite3.connect("db_university.db")

c = conn.cursor()
#c.execute("DROP TABLE student;")

c.execute("""CREATE TABLE student(
        name TEXT,
        age INTEGER,
        roll INTEGER,
        branch TEXT
        )""")

c.execute("INSERT INTO student VALUES('Mayank',21,01,'CSE')")
c.execute("INSERT INTO student VALUES('Sahil',20,02,'CSE')")
c.execute("INSERT INTO student VALUES('Rohit',21,03,'CSE')")
c.execute("INSERT INTO student VALUES('Mahesh',22,04,'CSE')")
c.execute("INSERT INTO student VALUES('Kamlesh',21,05,'CSE')")
c.execute("INSERT INTO student VALUES('Rishabh',20,06,'CSE')")
c.execute("INSERT INTO student VALUES('Virat',21,07,'CSE')")
c.execute("INSERT INTO student VALUES('Dhoni',23,08,'CSE')")
c.execute("INSERT INTO student VALUES('Messi',21,09,'CSE')")
c.execute("INSERT INTO student VALUES('Ronaldo',22,10,'CSE')")

c.execute("SELECT * FROM student")
print ( c.fetchall() )


c.execute("SELECT * FROM student")

from pandas import DataFrame

df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]
