#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:31:34 2020

@author: surmayi.shree
"""

print('This is Simple Linear Regression Implementation')

import numpy as np
from math import sqrt

class SimpleLinearRegression:
        def calculateMean(self,values):
            return sum(values)/float(len(values))
        
        def calculateVariance(self,data,mean):
            return sum((val - mean)**2 for val in data)
        
        def calculateCovariance(self,X,Y,X_mean,Y_mean):
            covar = 0.0 
            for i in range(0,len(X)):
                covar+=((X[i]-X_mean) *(Y[i]-Y_mean))
            return covar
        
        def calculateCoefficients(self,X_train, Y_train):
            
            X_mean = self.calculateMean(X_train)
            Y_mean = self.calculateMean(Y_train)
            
            coef1 = self.calculateCovariance(X_train, Y_train,X_mean,Y_mean) /self.calculateVariance(X_train, X_mean)
            coef0 = Y_mean - coef1* X_mean
            
            return coef0, coef1
            
        def predictY(self,X_train, Y_train,X_test):
            coef0, coef1 = self.calculateCoefficients(X_train,Y_train)
            predictions = []
            for x in X_test:
                predictions.append(coef0 + coef1* x)
            return predictions
            
        def calculateCost(self, Y_test, predictions):
            error = 0
            for i in range(0,len(Y_test)):
                error+=(predictions[i]-Y_test[i])**2
            return (error / float(len(Y_test)))
        
        def split_train_test(self,data,portion):
            train = data[0: int(len(data)*portion)]
            test = data[int(len(data)*portion): int(len(data))]
            X_train = [train[i][0] for i in range(len(train))]
            Y_train = [train[i][1] for i in range(len(train))]
            X_test = [test[i][0] for i in range(len(test))]
            Y_test = [test[i][1] for i in range(len(test))] 
            
            return X_train, Y_train, X_test, Y_test
        
        
ls =  SimpleLinearRegression()
data = np.random.randint(0,100,30)
data = data.reshape(15,2)
print(data)
X_train, Y_train, X_test, Y_test  = ls.split_train_test(data, 0.75)   

print('X_train, Y_train, X_test, Y_test ', X_train, Y_train, X_test, Y_test )

predictions =   ls.predictY(X_train, Y_train, X_test)
print('Predictions: ', predictions)
cost = ls.calculateCost( Y_test, predictions)
print('Cost: ', cost)
print('Mean Squared error : ', str(cost))
print('Root mean Sqaured error: ',str(sqrt(cost)))
        
        