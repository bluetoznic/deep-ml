import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# ---------- 标准化 ----------
    mea = data.mean(axis=0)
    st = data.std(axis=0)
    standardized_data = (data - mea) / st

    # ---------- 最小-最大归一化 ----------
    mind = data.min(axis=0)
    maxd = data.max(axis=0)
    normalized_data = (data - mind) / (maxd - mind)

    # ---------- 四舍五入到 4 位小数 ----------
    standardized_data = np.round(standardized_data, 4)
    normalized_data = np.round(normalized_data, 4)

    return standardized_data, normalized_data