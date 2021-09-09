import numpy as np

class Perceptron:
	def __init__(self, X, W, bias):
		self.X = X
		self.W = W	
		self.bias = bias

	def calculateV(self):
		"""
		Returns the multiplication of W matrix and X matrix
		"""
		return np.dot(self.X, self.W) - self.bias

	def activation(self):
		"""
		Implementation of the step function
		"""
		V = self.calculateV()
		Y = np.zeros((V.shape[0],1))

		for i in range(V.shape[0]):
			Y[i] = 1 if V[i] >= 0 else 0

		return Y
