# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:41:29 2019

@author: Sahil
"""
"""
*****
Classification Code Challenge
*****

tree_addhealth.csv

Q1. (Create a program that fulfills the following specification.)

For this Code Challenge, The National Longitudinal Study of Adolescent to Adult Health (Add Health) data set, an ongoing (longitudinal) survey study that began in the mid-1990s is used. The project website URL is:

http://www.cpc.unc.edu/projects/addhealth/.

This large data set is available online from the University of North Carolina’s Carolina Population Center, http://www.cpc.unc.edu/projects/addhealth/data.

 

Import tree_addhealth.csv

 

The attributes are:

 

BIO_SEX: 1 = male 0 = female    

HISPANIC: 1=Yes,0=No    

WHITE : 1=Yes,0=No

BLACK : 1=Yes,0=No          

NAMERICAN: 1=Yes,0=No                      

ASIAN: 1=Yes,0=No                      

ALCEVR1: ever drank alcohol(1=Yes,0=No)   

marever1: ever smoked marijuana(1=Yes,0=No)    

cocever1: ever used cocaine(1=Yes,0=No)                

inhever1: ever used inhalants(1=Yes,0=No)             

cigavail: cigarettes available in home(1=Yes,0=No)

PASSIST: parents or public assistance(1=Yes,0=No)

EXPEL1: ever expelled from school(1=Yes,0=No)

TREG1: Ever smoked regularly(1=Yes,0=No)

Explanatory Variables:

Age

ALCPROBS1:alcohol problems 0-6

DEP1: depression scale

ESTEEM1: self esteem scale       

VIOL1:violent behaviour scale

DEVIANT1: deviant behaviour scale     

SCHCONN1: school connectedness scale       

GPA1: gpa scale  4 points)

FAMCONCT: family connectedness scale       

PARACTV:parent activities scale

PARPRES:parental presence scale

 

    Build a classification tree model evaluating if an adolescent would smoke regularly or not based on: gender, age, (race/ethnicity) Hispanic, White, Black, Native American and Asian, alcohol use, alcohol problems, marijuana use, cocaine use, inhalant use, availability of cigarettes in the home, depression, and self-esteem.

    Build a classification tree model evaluation if an adolescent gets expelled or not from school based on their Gender and violent behavior.
    Use random forest in relation to regular smokers as a target and explanatory variable specifically with Hispanic, White, Black, Native American and Asian.

(Please make confusion matrix and also check accuracy score for each and every section)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_csv("tree_addhealth.csv")

dataset.isnull().any(axis=0)


#mean = dataset['age'].mean()
#dataset['age'] = dataset['age'].fillna(mean)


#removing nan
dataset = dataset.fillna(dataset.mean()) 

#1
columns_name = list(dataset.columns)
print(columns_name)


labels = dataset.iloc[:,7].values

features = dataset.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]].values

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features, labels)

#Calculate Class Probabilities
probability = classifier.predict_proba(features)


# Predicting the class labels
labels_pred = classifier.predict(features)


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels, labels_pred)
print(cm)


score = classifier.score(features, labels)
print("Score: ", score*100)


#2





labels2 = dataset.iloc[:,21].values

features2 = dataset.iloc[:,[0,16]].values



classifier.fit(features2, labels2)



#Calculate Class Probabilities
probability2 = classifier.predict_proba(features2)


# Predicting the class labels
labels_pred2 = classifier.predict(features2)


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels2, labels_pred2)
print(cm)


score = classifier.score(features2, labels2)
print("Score: ", score*100)












"""
#3



labels3 = dataset.iloc[:,7].values

features3 = dataset.iloc[:,1:6].values

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features3, labels3)


#Calculate Class Probabilities
probability3 = classifier.predict_proba(features3)

# Predicting the class labels
labels_pred3 = classifier.predict(features3)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels3, labels_pred)

"""




























