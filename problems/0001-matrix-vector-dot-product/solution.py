def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
   # 空矩阵处理
    if not a:
        return []

    # 列数与 b 长度不匹配
    if len(a[0]) != len(b):
        return -1

    # 维度匹配，正常计算点积
    return [sum(x * y for x, y in zip(row, b)) for row in a]


	