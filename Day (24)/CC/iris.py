# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:47:31 2019

@author: Sahil
"""

"""
Q2. (Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, Iris virginica and Iris versicolor).



    Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the following command:\


from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data



Reduce dimension from 4-d to 2-d and perform clustering to distinguish the 3 species.
"""

import numpy as np 
import pandas as pd 


from sklearn import datasets 
iris = datasets.load_iris ()

iris.feature_names
iris.target


dataset	= pd.DataFrame (iris.data, columns= iris.feature_names )
dataset['Species']= iris.target

#dataset['Versicolor']= iris.target
#dataset['Virginica']= iris.target


features = dataset.iloc[:,0:4].values
labels = dataset.iloc[:,4:].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


#PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)
explained_variance = pca.explained_variance_ratio_




from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)






#Clustering

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans

# 2d data used
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features_train)
    wcss.append(kmeans.inertia_)    

import matplotlib.pyplot as plt
#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()



# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features_train)


# Visualising the clusters

plt.scatter(features_train[pred_cluster == 0, 0], features_train[pred_cluster == 0, 1], c = 'blue', label = 'setosa')
plt.scatter(features_train[pred_cluster == 1, 0], features_train[pred_cluster == 1, 1], c = 'red', label = 'versicolor')
plt.scatter(features_train[pred_cluster == 2, 0], features_train[pred_cluster == 2, 1], c = 'green', label = 'virginica')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()
