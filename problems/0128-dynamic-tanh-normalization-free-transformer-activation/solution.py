import numpy as np

def dynamic_tanh(x: np.ndarray, alpha: float, gamma: float, beta: float) -> list[float]:
    # Your code here
    y=gamma * np.tanh(alpha*x)+beta
    return y.tolist()