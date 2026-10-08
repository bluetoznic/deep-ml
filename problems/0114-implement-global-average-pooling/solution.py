import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
	average_arr=np.mean(x,axis=(0,1))
	return average_arr