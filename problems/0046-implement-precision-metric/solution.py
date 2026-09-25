import numpy as np
def precision(y_true, y_pred):
  # 真正例：预测为 1 且真实为 1
    tp = np.sum((y_true == 1) & (y_pred == 1))
    # 假正例：预测为 1 但真实为 0
    fp = np.sum((y_true == 0) & (y_pred == 1))
    
    # 避免除以零
    if tp + fp == 0:
        return 0.0
    
    return float(tp / (tp + fp))
