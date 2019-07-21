# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:04:53 2019

@author: Sahil
"""

"""
Q1. (Create a program that fulfills the following specification.)

Import Crime.csv File.

    Perform dimension reduction and group the cities using k-means based on Rape, Murder and assault predictors.

"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_csv("crime_data.csv")

features = dataset.iloc[:, [1,2,4]].values
#labels = dataset.iloc[:, 0].values


#1



# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)
explained_variance = pca.explained_variance_ratio_






#2


from sklearn.cluster import KMeans

"""
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
"""


# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)




# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Low Crime')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'High Crime')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Med Crime')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Crime_Data')
plt.xlabel('P1_Feature')
plt.ylabel('P2_Feature')
plt.legend()
plt.show()