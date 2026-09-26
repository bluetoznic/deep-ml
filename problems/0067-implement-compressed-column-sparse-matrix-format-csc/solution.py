import numpy as np
def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	d=np.array(dense_matrix)
	rows,cols=d.shape

	row_idx,col_idx=np.nonzero(d)
    #get values
	vals=d[row_idx,col_idx]
	ac=np.argsort(col_idx)
	vals=vals[ac]
	row_idx=row_idx[ac]
	#get  counts in rows for nonzero
	counts=np.bincount(col_idx,minlength=cols) #(1,1,1,1)eg
	col_ptr=np.concatenate(([0], np.cumsum(counts)))

	return vals.tolist(), row_idx.tolist(), col_ptr.tolist()





