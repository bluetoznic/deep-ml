import numpy as np

def shuffle_data(X, y, seed=None):
    if seed is not None:
        np.random.seed(seed)          # 旧版全局种子
    idx = np.random.permutation(len(X))   # 旧版 permutation
    return X[idx], y[idx]