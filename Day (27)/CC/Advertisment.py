# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:22:51 2019

@author: Sahil
"""
"""
Q1. 

(Click Here To Download Training data File): 
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json

(Click Here To Download Test data File):
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json


This is the data for local classified advertisements. It has 9 prominent sections: jobs, resumes, gigs, personals, housing, community, services, for-sale and discussion forums. Each of these sections is divided into subsections called categories. For example, the services section has the following categories under it:
beauty, automotive, computer, household, etc.

For a set of sixteen different cities (such as newyork, Mumbai, etc.), we provide to you data from four sections

        for-sale
        housing
        community
        services

and we have selected a total of 16 categories from the above sections.

        activities
        appliances
        artists
        automotive
        cell-phones
        childcare
        general
        household-services
        housing
        photography
        real-estate
        shared
        temporary
        therapeutic
        video-games
        wanted-housing

Each category belongs to only 1 section.

About Data:

        city (string) : The city for which this Craigslist post was made.
        section (string) : for-sale/housing/etc.
        heading (string) : The heading of the post.

each of the fields have no more than 1000 characters. The input for the program has all the fields but category which you have to predict as the answer.

A total of approximately 20,000 records have been provided to you, proportionally represented across these sections, categories and cities. The format of training data is the same as input format but with an additional field "category", the category in which the post was made.

Task:

    Given the city, section and heading of an advertisement, can you predict the category under which it was posted?
    Also Show top 5 categories which has highest number of posts
    
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#data = pd.read_json("Advertisement_test_data.json")    #make array in file

train = pd.read_json('train.json',lines =True , orient = 'columns' )            #copy paste in new file

test = pd.read_json('test.json' ,lines =True , orient = 'columns')


features_train = train.iloc[:,1:]

labels_train = train.iloc[:,0]

import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords


from nltk.stem.porter import PorterStemmer

corpus = []

for i in range(0, 20217):
    review = re.sub('[^a-zA-Z]', ' ', features_train['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
   
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
   
    review = ' '.join(review)
    corpus.append(review)

    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features_train2 = cv.fit_transform(corpus).toarray()



from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train2, labels_train)


labels_pred = classifier.predict(test)