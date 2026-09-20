def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	if not matrix:
		return []
	
	return [[arr*scalar for arr in row] for row in matrix]