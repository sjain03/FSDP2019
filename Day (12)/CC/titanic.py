# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:48:26 2019

@author: Sahil
"""

"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""

import pandas as pd

df = pd.read_csv("training_titanic.csv")



#no of passenger survived or died
survived_died  = df['Survived'].value_counts()


print("Survived :", survived_died[0] )

print("Died :", survived_died[1] )



#percent of passenger survived or died
percent  = df['Survived'].value_counts(normalize = True)     
percent = percent * 100
print("Survived :", percent[0] )

print("Died :", percent[1] )


#percent of male passenger survived or died
df_male = df[df['Sex'] == 'male' ] [['Survived']]

male_percent = df_male['Survived'].value_counts(normalize = True)
male_percent = male_percent*100

print("Male Survived Percentage :", male_percent[0] )
print("Male Died Percentage :", male_percent[1] )




#percent of female passenger survived or died
df_female = df[df['Sex'] == 'female' ] [['Survived']]

female_percent = df_female['Survived'].value_counts(normalize = True)
female_percent = female_percent*100

print("Female Survived Percentage :", female_percent[0] )

print("Female Died Percentage :", female_percent[1] )





#add new child column

df["child"] = df["Age"].map(lambda x: 0 if x >= 18 else 1 )




#percent of child passenger survived or died
df_child = df[df['child'] == 1 ] [['Survived']]

child_survive = df_child['Survived'].value_counts(normalize = True)
child_survive = child_survive * 100

#percent of adult passenger survived or died
df_adult = df[df['child'] == 0 ] [['Survived']]

adult_survive = df_adult['Survived'].value_counts(normalize = True)
adult_survive = adult_survive*100



print("Child Survived Percentage :", child_survive[1] )

print("Adult Survived Percentage :", adult_survive[1] )

