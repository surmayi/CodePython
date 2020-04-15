""" Implementing LogisticsRegression WIth Regularization

author : surmayi

pred = 1./(1+ e.^ -(X*theta))

theta_reg = [0;theta(2:n+1)]
reg = (lambda/(2*m))* theta_reg'*theta_reg

J= -1/m* (y'*log(pred) + (1-y)'* log(1-pred)) + reg
grad = (1/m)*(X'*(pred - y)+ lambda*theta_reg)

"""
import numpy as np

class LinearRegressionWithRegularization:
    
    def sigmoid(self,theta,X_train):
        z= X_train.dot(theta.T)
        return 1/(1 + np.exp(-1*z))
    
    def calculateRegularizationParam(self,lambdah,theta,m):
        theta[0] = 0
        reg = lambdah/(2*m) * theta.dot(theta.T)
        return reg 
    
    def calculateCostWithReg(self,m,lambdah,theta,Y_train,prediction):
        reg = self.calculateRegularizationParam(lambdah,theta,m)
        return -1/m * (Y_train.dot(np.log(prediction.T)) + (1-Y_train).dot(np.log(1-prediction.T))) + reg
    
    def calculateGradient(self,m,X_train, prediction, Y_train, lambdah,theta):
        theta[0] = 0
        return 1/m * ((prediction-Y_train).dot(X_train) + lambdah* theta)
    
    
    
lgr = LinearRegressionWithRegularization()

Y_train = np.array([1,0,1,1])

X_train = np.array([[1, 1, 7, 3],
       [3, 3, 1, 6],
       [7, 2, 5, 8],
       [4, 3, 7, 7]])
theta = np.array([1,1,1,1])

lambdah = 10

m = len(Y_train)

prediction = lgr.sigmoid(theta,X_train) 
print(prediction)   

cost = lgr.calculateCostWithReg(m,lambdah,theta,Y_train,prediction)
print(cost)

grad = lgr.calculateGradient(m,X_train,prediction, Y_train,lambdah, theta)
print(grad)