import numpy as np

def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    arr=np.array(x)

    mina=np.min(arr)
    maxa=np.max(arr)

    if mina==maxa:
        return [0.0]*len(x)
    
    scaled_arr=(arr-mina)/(maxa-mina)

    return scaled_arr