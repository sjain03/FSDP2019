# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:20:00 2019

@author: Sahil
"""


"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""

fp = open("zoo.csv","rt")

a = fp.readlines()
print(a)

#1
import csv

with open("zoo.csv","rt") as fp:
    csv_reader = csv.reader(fp,delimiter=',')
    
    for row in csv_reader:
        print(row)
#2    
with open("zoo.csv","rt") as fp:
    csv_reader = csv.reader(fp,delimiter=",")
    
    for column in csv_reader:
        for i in range(len(column)):
            print(column[i])
            
#3
with open("zoo.csv","rt") as fp:
    csv_reader = csv.reader(fp,delimiter=',')
    
    total_water_needed = 0
    next(csv_reader)
    
    for column in csv_reader:
        total_water_needed = int(column[2]) + total_water_needed
print("total water needed by all the animals" +str (total_water_needed))


#4
with open("zoo.csv","rt") as fp:
    csv_reader = csv.reader(fp,delimiter=',')
    
    water_elephants = 0
    water_tigers = 0
    water_zebras = 0
    water_lions = 0
    water_kangaroos =0
    
    next(csv_reader)
    
    for column in csv_reader:
        
        if column[0] == "elephant":
            water_elephants = int(column[2]) + water_elephants
        if column[0] == "tiger":
            water_tigers = int(column[2]) + water_tigers
        if column[0] == "zebra":
            water_zebras = int(column[2]) + water_zebras
        if column[0] == "lion":
            water_lions = int(column[2]) + water_lions
        if column[0] == "kangaroo":
            water_kangaroos = int(column[2]) + water_kangaroos
            
print("water needed by elephants :" + str(water_elephants))
print("water needed by tigers :" + str(water_tigers))
print("water needed by zebras :" + str(water_zebras))
print("water needed by lions :" + str(water_lions))
print("water needed by kangaroos :" + str(water_kangaroos))


#5
            
with open('zoo.csv','rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    total_water_needed_elephant = 0
    total_water_needed_tiger = 0
    total_water_needed_zebra = 0
    total_water_needed_lion = 0
    total_water_needed_kangaroo = 0


    # Use the below line to skip the header line from the csv file 
    next(csv_reader) 
    for column in csv_reader:
        if column[0]=="elephant":
            total_water_needed_elephant = int(column[2])+total_water_needed_elephant
        if column[0]=="tiger":
            total_water_needed_tiger = int(column[2])+total_water_needed_tiger
        if column[0]=="zebra":
            total_water_needed_zebra = int(column[2])+total_water_needed_zebra
        if column[0]=="lion":
            total_water_needed_lion = int(column[2])+total_water_needed_lion
        if column[0]=="kangaroo":
            total_water_needed_kangaroo = int(column[2])+total_water_needed_kangaroo
            
animal_dictionary = {}

animal_dictionary["elephant"]=total_water_needed_elephant
animal_dictionary["tiger"]=total_water_needed_tiger
animal_dictionary["zebra"]=total_water_needed_zebra
animal_dictionary["lion"]=total_water_needed_lion
animal_dictionary["kangaroo"]=total_water_needed_kangaroo

print (animal_dictionary)