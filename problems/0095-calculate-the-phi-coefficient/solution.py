import numpy as np
def phi_corr(x: list[int], y: list[int]) -> float:
    yt = np.array(x)
    yp = np.array(y)
    tp = np.sum((yt == 1) & (yp == 1))
    tn = np.sum((yt == 0) & (yp == 0))
    fp = np.sum((yt == 0) & (yp == 1))
    fn = np.sum((yt == 1) & (yp == 0))

    numerator = tp * tn - fp * fn
    denominator = np.sqrt(
        (tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)
    )

    if denominator == 0:
        return 0.0

    phi = numerator / denominator
    return round(float(phi), 4)
