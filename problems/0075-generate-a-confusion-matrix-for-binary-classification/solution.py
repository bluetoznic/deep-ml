import  numpy as np
from collections import Counter

def confusion_matrix(data):
    data = np.array(data)
    y_true = data[:, 0]
    y_pred = data[:, 1]

    TN = np.sum((y_true == 0) & (y_pred == 0))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))
    TP = np.sum((y_true == 1) & (y_pred == 1))

    return [[int(TP), int(FN)], [int(FP), int(TN)]]
