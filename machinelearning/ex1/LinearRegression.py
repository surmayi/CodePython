#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:31:34 2020

@author: surmayi.shree
"""


print('This is Linear Regression With Gradient Descent')
import numpy as np

class LinearRegressionGradientDescent:
    
    def calculatePrediction(self,X_train, theta):
        return X_train.dot(theta)
    
    def calculateCostOverTheta(self, X_train,Y_train, theta):
        prediction = self.calculatePrediction(X_train, theta)
        print('Prediction: ', prediction)
        return prediction, sum((prediction-Y_train)**2)/(2*float(len(Y_train)))

    def calculateGradient(self,theta,alpha,prediction,Y_train):
        return theta - (alpha * X_train.T.dot(prediction-Y_train))/float(len(theta))
    
    def split_train_test(self,X,Y,portion):
        size = int(len(X)*portion)
        X_train = [X[:size]]
        Y_train = [Y[:size]]
        X_test = [X[size,len(X)]]
        Y_test = [Y[size,len(Y)]]
        return X_train, Y_train, X_test, Y_test
    
lg =  LinearRegressionGradientDescent()

Y_train = [11 ,14, 22, 22]

X_train = np.array([[1, 1, 7, 3],
       [3, 3, 1, 6],
       [7, 2, 5, 8],
       [4, 3, 7, 7]])
theta = np.array([1,1,1,1])

#X_train, Y_train, X_test, Y_test = lg.split_train_test(X,Y,0.75)

alpha = 0.01
curcost = []
for i in range(0,100):
    prediction, cost = lg.calculateCostOverTheta(X_train, Y_train,theta)
    curcost.append(cost)
    print('Cost in this loop is: ', str(curcost[i]))
    print('Previous cost: ', curcost[i-1])
    if(curcost[i]>curcost[i-1]):
        break
    if(curcost[i]>0):
        cost = -1*curcost[i]
    theta = lg.calculateGradient( theta,alpha, prediction, Y_train)
    print('Gradient in this loop is: ', theta)
    
print('Minimun cost: ', min(curcost))