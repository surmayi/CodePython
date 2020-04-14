#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:56:34 2020

@author: surmayi.shree
"""



# -*- coding: utf-8 -*-
# ====================== YOUR CODE HERE ======================
# Instructions: First, for each feature dimension, compute the mean
#               of the feature and subtract it from the dataset,
#               storing the mean value in mu. Next, compute the
#               standard deviation of each feature and divide
#               each feature by it's standard deviation, storing
#               the standard deviation in sigma.
#
#               Note that X is a matrix where each column is a
#               feature and each row is an example. You need
#               to perform the normalization separately for
#               each feature.
#
# Hint: You might find the 'mean' and 'std' functions useful.
#
import numpy as np 

X_train = np.array([[1, 1, 7, 3],
       [3, 3, 1, 6],
       [7, 2, 5, 8],
       [4, 3, 7, 7]])

X_temp = X_train.T

X_mean = []
X_std = []

for row in X_temp:
    X_mean.append(np.mean([row]))
    X_std.append(np.std([row]))

print(X_mean)
print(X_std)

for i in range(len(X_temp)):
    for j in range(0,len(X_temp[i])):
        X_temp[i][j] = (X_temp[i][j]-float(X_mean[j]))/float(X_std[j])
    
print(X_temp)
X_train = X_temp.T
print(X_train)
