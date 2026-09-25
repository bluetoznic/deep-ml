import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	d=np.array(dense_matrix)
	row,col=d.shape
	row_idx,col_idx=np.nonzero(d)
	values=d[row_idx,col_idx]
	counts=np.bincount(row_idx,minlength=row)
	countsplus=np.cumsum(counts)
	rawpoint=np.concatenate(([0],countsplus))
	return values.tolist(), col_idx.tolist(), rawpoint.tolist()

