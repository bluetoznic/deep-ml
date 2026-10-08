import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    # Your code here
    p=np.array(p)
    q=np.array(q)

    if len(p)!=len(q):
        return 0.0

    bc=np.sum(np.sqrt(p*q))

    if bc<=0:
        return 0.0

    return float(-np.log(bc))