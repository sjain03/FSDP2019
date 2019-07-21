# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:32:50 2019

@author: Sahil
"""
"""
Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

    Perform K-means clustering to distinguish urban drivers and rural drivers.
    Perform K-means clustering again to further distinguish speeding drivers from those who follow speed limits, in addition to the rural vs. urban division.
    Label accordingly for the 4 groups.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_csv("deliveryfleet.csv")
features = dataset.iloc[:,[1,2]].values

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans

wcss =[]
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = "k-means++", random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

#1

kmeans = KMeans(n_clusters = 2, init = "k-means++", random_state = 0 )
pred_cluster = kmeans.fit_predict(features)


# Visualising the clusters

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Rural')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Urban')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance_Feature')
plt.ylabel('Speeding_Feature')
plt.legend()
plt.show()




#2

kmeans = KMeans(n_clusters = 4, init = "k-means++", random_state = 0 )
pred_cluster = kmeans.fit_predict(features)



# Visualising the clusters

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Rural follow speed limit')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Urban follow speed limit')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'brown', label = 'Rural follow speed limit')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'black', label = 'Speed_')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance_Feature')
plt.ylabel('Speeding_Feature')
plt.legend()
plt.show()

