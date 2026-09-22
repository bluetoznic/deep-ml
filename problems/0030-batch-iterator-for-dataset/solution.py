import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	for i in range(0,len(X),batch_size):
		if y is None:
			yield [X[i:i+batch_size].tolist()]
		else:
		    yield [X[i:i+batch_size], y[i:i+batch_size].tolist()]
	