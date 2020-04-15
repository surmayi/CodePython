""" Implementing LogisticsRegression

author : surmayi

J = -1/m * (y'*log(pred)+ (1-y)'*log(1-pred))
grad = (1/m)*X'*(pred - y)

"""
import numpy as np

class LogisticsRegression:
    
    def sigmoid(self,theta,X_train):
        z= X_train.dot(theta.T)
        return 1/(1 + np.exp(-1*z))
    
    def calculateCost(self, prediction, Y_train):
        m = len(Y_train)
        cost = -1/m *(Y_train.dot(np.log(prediction.T)) + (1-Y_train).dot(np.log(1-prediction.T)))
        return cost
    
    def calculateGradient(self,prediction,Y_train,X_train):
        m = len(Y_train)
        return 1/m * X_train.T.dot(prediction-Y_train)
        
    
Y_train = np.array([1,0,1,1])

X_train = np.array([[1, 1, 7, 3],
       [3, 3, 1, 6],
       [7, 2, 5, 8],
       [4, 3, 7, 7]])
theta = np.array([1,1,1,1])


lg = LogisticsRegression()

prediction = lg.sigmoid(theta,X_train) 
print(prediction)   

cost = lg.calculateCost(prediction,Y_train)
print(cost)

grad = lg.calculateGradient(prediction,X_train, Y_train)
print(grad)