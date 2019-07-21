# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:11:27 2019

@author: Sahil
"""
"""
Q1. Code Challegene (NLP)
Dataset: amazon_cells_labelled.txt


The Data has sentences from Amazon Reviews

Each line in Data Set is tagged positive or negative

Create a Machine learning model using Natural Language Processing that can predict wheter a given review about the product is positive or negative
"""

import pandas as pd

dataset = pd.read_csv("amazon_cells_labelled.txt", delimiter ='\t',header = None)

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer


corpus = []

for i in range (0,1000):
    review = re.sub('[^a-zA-Z]',' ',dataset[0][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review 
              if not word
              in set (stopwords.words('english'))]
    
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    
    review = ' '.join(review)
    corpus.append(review)

 
#Encoding
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)



# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_nb = confusion_matrix(labels_test, labels_pred)








# Fitting Kernel SVM to the Training set
# kernels: linear, poly and rbf
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)