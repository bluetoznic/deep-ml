import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	arrx=np.array(X,dtype=float)
	arry=np.array(y,dtype=float)
	theta=np.linalg.pinv(arrx.T @ arrx) @ arrx.T @ arry

	result=[round(float(v),4)+0.0 for v in theta]
	return result