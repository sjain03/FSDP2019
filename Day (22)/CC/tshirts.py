# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:35:37 2019

@author: Sahil
"""

"""
Q1. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. How would you figure out the actual size of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_csv("tshirts.csv")
features = dataset.iloc[:,[1,2]].values


#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

from sklearn.preprocessing import StandardScaler
features = StandardScaler().fit_transform(features)

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


kmeans = KMeans(n_clusters = 3, init = "k-means++", random_state = 0 )
pred_cluster = kmeans.fit_predict(features)



# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Small')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Medium')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Large')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
plt.show()






















"""
from sklearn.cluster import DBSCAN
# Compute DBSCAN
db = DBSCAN(eps=0.1, min_samples=2).fit(features)

labels_pred = db.labels_

import matplotlib.pyplot as plt


plt.scatter(features[labels_pred == 0,0], features[labels_pred == 0,1],c='r', marker='+' )
plt.scatter(features[labels_pred == 1,0], features[labels_pred == 1,1],c='g', marker='o' )
plt.scatter(features[labels_pred == 2,0], features[labels_pred == 2,1],c='b', marker='s' )
plt.scatter(features[labels_pred == -1,0],features[labels_pred == -1,1],c='y', marker='*' )
"""
