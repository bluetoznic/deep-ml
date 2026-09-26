import numpy as np
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	prolength=np.dot(v,L)/np.linalg.norm(L)
	nornL=L/np.linalg.norm(L)
	vec=nornL*prolength
	return vec
