"""

function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1)
num_labels = size(Theta2, 1)

% You need to return the following variables correctly
p = zeros(size(X, 1), 1)
X = [ones(m,1) X]
Theta1
Theta2
% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned neural network. You should set p to a
%               vector containing labels between 1 to num_labels.
%
% Hint: The max function might come in useful. In particular, the max
%       function can also return the index of the max element, for more
%       information see 'help max'. If your examples are in rows, then, you
%       can use max(A, [], 2) to obtain the max for each row.
%

a2 = sigmoid(X*Theta1')

a2 = [ones(size(a2,1),1) a2]

a3 = sigmoid(a2*Theta2')

[p_max, p] = max(a3,[],2)

"""
import numpy as np

class NeuralNetwork2Layer:
    
    def sigmoid(self,theta,X_train):
        z= X_train.dot(theta.T)
        return 1/(1 + np.exp(-1*z))

nn = NeuralNetwork2Layer()

X_train = np.array([[1, 1, 7],
       [3, 3, 1],
       [7, 2, 5],
       [4, 3, 7]])
theta1 = np.array([[1,1,1,1],[2,2,2,2]])
theta2 = np.array([[1,1,1,1]])

m1 = len(X_train)
X_train = np.concatenate((np.array(np.ones((m1), dtype=int)),X_train.T.ravel())).reshape(4,4).T

a2 = nn.sigmoid(theta1,X_train)

m2 = len(a2)

a2 = np.concatenate((np.array(np.ones((m2), dtype=int)),a2.T.ravel())).reshape(4,3).T

a3 = nn.sigmoid(theta2,a2)
m3 = len(a3)

print(max(a3))











