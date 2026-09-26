
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here

	rmse_res=np.sqrt((1/y_pred.size)*(np.sum((y_pred-y_true)**2)))
	return round(rmse_res,3)
