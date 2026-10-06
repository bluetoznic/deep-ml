import numpy as np
def calculate_f1_score(y_true, y_pred):

    yt = np.array(y_true)
    yp = np.array(y_pred)
    tp = np.sum((yt == 1) & (yp == 1))
    fp = np.sum((yt == 0) & (yp == 1))
    fn = np.sum((yt == 1) & (yp == 0))

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall    = tp / (tp + fn) if (tp + fn) > 0 else 0.0

    if precision + recall == 0:
        return 0.0

    f1 = 2 * precision * recall / (precision + recall)
    return round(f1, 3)