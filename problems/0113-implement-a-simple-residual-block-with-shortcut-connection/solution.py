import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
	# Your code here
	x1=np.maximum(0,np.dot(x,w1))
	x2=np.maximum(0,np.dot(x,w2))

	return np.maximum(0.0,x1+x2)
