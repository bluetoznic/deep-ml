import numpy as np

def make_diagonal(x):
	# Your code here
	result=np.zeros((len(x),len(x)),dtype=x.dtype)
	result[np.arange(len(x)),np.arange(len(x))]=x
	return result.tolist()
	