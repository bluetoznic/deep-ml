import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	s=np.array(scores)
	shift=s-np.max(s)
	return s-np.max(s)-np.log(np.sum(np.exp(shift)))
	