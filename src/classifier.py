class Perceptron:
	def __init__(self, X, W):
		self.X = X
		self.W = W	

	def calculateV(self):
		"""
		Returns the multiplication of W matrix and X matrix
		"""
		return np.dot(self.W, self.X)

	def activation(self):
		"""
		Implementation of the step function
		"""
		V = self.calculateV()
		Y = np.zeros((V.shape[0],1))

		for i in range(V.shape[0]):
			Y[i] = 1 if V[i] >= 0 else 0

		return Y

	def getX(self):
		pass

	def getW(self):
		pass

