
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	iou=np.sum((y_true==1)&(y_pred==1))
	n1=np.sum(y_true==1)
	n2=np.sum(y_pred==1)
	if (n1+n2)==0:
		return 0.0
	else:
	    res=(2*iou)/(n1+n2)
	return round(res, 3)
