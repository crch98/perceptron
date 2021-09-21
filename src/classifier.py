import numpy as np

class Perceptron:
    def __init__(self, W, expected, lr=0.1):
        #self.X = X
        #self.W = np.array([[bias], [W[0]], [W[1]]])
        self.W = W
        self.expected = expected
        self.lr = lr

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
        for xi, target in zip(X, self.expected):
            update = self.lr * (target - self.activation(xi))
            self.W[1:] += update * xi
            self.W[0] += update
            #print(self.W)


# def main():
#     X = np.array([[1, 1], [-0.5, 1], [3, 1], [-2, 1]])
#     target = np.array([[1], [-1], [1], [-1]])
#     #w = np.random.rand(1, 3)
#     w = np.array((1, -2.5, 1.75))
#     p = Perceptron(w, target, 0.5)

#     p.train(X, target)


# main()
