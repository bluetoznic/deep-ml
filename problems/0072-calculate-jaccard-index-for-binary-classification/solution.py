
import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
	iou=np.sum((y_true==1)&(y_pred==1))
	ou=np.sum((y_true==1)|(y_pred==1))
	if ou==0:
		return -1
	else:
		result=iou/ou
	return round(result, 3)
