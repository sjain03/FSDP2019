# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:31:03 2019

@author: Sahil
"""
"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""

import json

json_faculty = """
{
    "faculty1": {
        "fname": "Smita",
        "lname": "Ag",
        "department" : "Computer Science",
        "research" : ["ML","AI"],
        "phd" : true,
        "photo" :"https://www.organicspamagazine.com/2017/10/06/amanda-seyfried-interview/",
        "contact": [
            {
                "email": "Smita@gmail.com",
                "conatct_no": 7896541230
            }
        ]
        },
        
    "faculty2": {
        "fname": "Sanjay",
        "lname": "Mishra",
        "department" : "Computer Science",
        "research" : ["ML","Bigdata"],
        "phd" : false,
        "photo" :"https://www.organicspamagazine.com/2017/10/06/amanda-seyfried-interview/",
        "contact": [
            {
                "email": "Sanjay@gmail.com",
                "conatct_no": 7776541230
            }
        ]
    }
}
"""

with open("faculty.json", "w") as write_file:
    json.dump(json_faculty, write_file)



type(json_faculty)

my_faculty = json.loads(json_faculty)
type(my_faculty)



json_student = """
{
    "student": {
        "fname": "Aman",
        "lname": "Ag",
        "department" : "Computer Science",
        "interest" : ["ML","AI"],
        "photo" : ""
        "contact": [
            {
                "email": "aman@gmail.com",
                "conatct_no": 7898541230
            }
        ]
        }
}
"""

with open("student.json", "w") as write_file2:
    json.dump(json_student, write_file2)
