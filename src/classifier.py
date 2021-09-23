import numpy as np

class Perceptron:
    def __init__(self, W, expected, lr=0.1, epoch=40):
        self.W = W
        self.expected = expected
        self.lr = lr
        self.epoch = epoch

    def calculateV(self, X):
        """
        Returns the multiplication of W matrix and X matrix
        """
        return np.dot(X, self.W[1:]) + self.W[0]

    def activation(self, X):
        """
        Implementation of the step function
        """
        return np.where(self.calculateV(X) >= 0.0, 1, -1)

    def train(self, X):
        counter = 0

        for _ in range(self.epoch):
            for xi, target in zip(X, self.expected):
                error = (target - self.activation(xi))
                update = self.lr * error
                self.W[1:] += update * xi
                self.W[0] += update

    def get_weights(self):
        return self.W