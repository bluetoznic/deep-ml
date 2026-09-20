import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix:
        return []

    mt = np.array(matrix)

    if mode == 'column':
        return mt.mean(axis=0).tolist()
    elif mode == 'row':
        return mt.mean(axis=1).tolist()
    else:
        return []
	
	