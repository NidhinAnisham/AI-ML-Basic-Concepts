# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:28:18 2018

@author: NI389899
"""

import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
import pandas as pd

dataset = pd.read_csv('auto_mpg.csv',encoding = "latin1")
dataset_X = dataset.loc[:, "acceleration"].values
dataset_Y = dataset.loc[:,"mpg"].values

# Split the data into training/testing sets
dataset_X_train = dataset_X[:-20]
dataset_X_test = dataset_X[-20:]
dataset_X_train = dataset_X_train.reshape(len(dataset_X_train),1)
dataset_X_test = dataset_X_test.reshape(len(dataset_X_test),1)

# Split the targets into training/testing sets
dataset_Y_train = dataset_Y[:-20]
dataset_Y_test = dataset_Y[-20:]
dataset_Y_train = dataset_Y_train.reshape(len(dataset_Y_train),1)
dataset_Y_test = dataset_Y_test.reshape(len(dataset_Y_test),1)

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(dataset_X_train, dataset_Y_train)

# Make predictions using the testing set
dataset_Y_pred = regr.predict(dataset_X_test)

# The coefficients
print('Coefficients: ', regr.coef_)
print('Intercept: ', regr.intercept_)
print('Residues ',regr.residues_)

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(dataset_Y_test, dataset_Y_pred))

# Plot outputs
plt.scatter(dataset_X_test, dataset_Y_test,  color='black')
plt.plot(dataset_X_test, dataset_Y_pred, color='red', linewidth=3)
plt.show()