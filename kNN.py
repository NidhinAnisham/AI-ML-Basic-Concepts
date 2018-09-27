# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:02:21 2018

@author: NI389899
"""
from sklearn import neighbors
import pandas as pd
from sklearn.model_selection import cross_val_score, KFold
import numpy as np

#reading csv data
dataset = pd.read_csv('haberman.csv',encoding = "latin1")
dataset_X = dataset.iloc[:, 0:3].values #features
dataset_Y = dataset.iloc[:, 3].values #labels

# Split the data into training/testing sets
dataset_X_train = dataset_X[:-20]
dataset_X_test = dataset_X[-20:]

# Split the targets into training/testing sets
dataset_Y_train = dataset_Y[:-20]
dataset_Y_test = dataset_Y[-20:]

#creating an instance of Neighbours Classifier and fit the data.
knn=neighbors.KNeighborsClassifier()
knn.fit(dataset_X_train, dataset_Y_train)

# Calculating accuracy of model using k-fold cross validation
kf = KFold(n_splits=10)
scores = cross_val_score(knn, dataset_X, dataset_Y, cv=kf)
print("Accuracy Scores for 10 folds: ",scores)
avg_score = np.mean(scores)
print("Average Score: ",avg_score)