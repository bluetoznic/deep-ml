import numpy as np
def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	# Your code here
	apple=np.array(apples)
	_,counts=np.unique(apple,return_counts=True)
	pro=counts/apple.size
	y=1-np.sum(pro**2)
	return float(y)
