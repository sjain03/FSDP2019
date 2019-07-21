# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:21:27 2019

@author: Sahil
"""
"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in
an online mongo atlas database.
"""
"""

Link to url-encode special characters : https://ascii.cl/url-encoding.htm
"""
import pymongo



client = pymongo.MongoClient("mongodb://yourusername:dbpassword@cluster0-shard-00-00-iwpg4.mongodb.net:27017,cluster0-shard-00-01-iwpg4.mongodb.net:27017,cluster0-shard-00-02-iwpg4.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")



#mydb = client.yourdbname
mydb = client.db_university

def addStudent(name,age,roll,branch):
    #mydb.yourcollectionname.insert_one
    mydb.student.insert_one(
            {
            "name" : name,
            "age": age,
            "roll" : roll,
            "branch" : branch
            }
            )
    return "Student added succesfully"


addStudent('Mayank',21,1,'CSE')
addStudent('Sahil',20,2,'CSE')
addStudent('Rohit',21,3,'CSE')
addStudent('Mahesh',22,4,'CSE')
addStudent('Kamlesh',21,5,'CSE')
addStudent('Rishabh',20,6,'CSE')
addStudent('Virat',21,7,'CSE')
addStudent('Dhoni',23,8,'CSE')
addStudent('Messi',21,9,'CSE')
addStudent('Ronaldo',22,10,'CSE')


def fetch_all_student():
    user = mydb.student.find()
    for i in user:
        print (i)


fetch_all_student()
