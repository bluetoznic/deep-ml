import math
import numpy as np
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    f = np.array(features)      # (n_samples, n_features)
    w = np.array(weights)       # (n_features,)
    y = np.array(labels)        # (n_samples,)

    # 1. 线性组合 + sigmoid
    z = f @ w + bias
    probabilities = 1 / (1 + np.exp(-z))   # 用 np.exp，不是 math.exp

    # 2. MSE
    mse = np.mean((probabilities - y) ** 2)

    # 3. 对结果四舍五入（要真正赋值/构造新对象）
    probabilities = [round(float(p), 4) for p in probabilities]
    mse = round(float(mse), 4)

    return probabilities, mse