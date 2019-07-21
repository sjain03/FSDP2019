# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:47:18 2019

@author: Sahil
"""

"""
Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("bluegills.csv")

features = dataset.iloc[:,0 ].values.reshape(-1,1)

labels = dataset.iloc[:, 1].values.reshape(-1,1)


# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features, labels)



print (regressor.score(features, labels))


"""
pred = regressor.predict(features)



# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, pred, color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Age')
plt.ylabel('Height')
plt.show()
"""








# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)



from sklearn.linear_model import LinearRegression
regressor2 = LinearRegression()
regressor2.fit(features_poly, labels)


print (regressor2.score(features_poly, labels))


"""
pred2 = regressor2.predict(poly_object.transform(features))


# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, pred2, color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Age')
plt.ylabel('Height')
plt.show()
"""




#2

x = np.array(5).reshape(1,-1)
height_pred = regressor2.predict(poly_object.transform(x))