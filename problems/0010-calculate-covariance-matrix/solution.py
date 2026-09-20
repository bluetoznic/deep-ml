def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:

	means=[sum(f)/len(vectors[0]) for f in vectors]

	n=len(vectors[0])

	m=len(vectors)
    
	conv=[[0]*m for _ in range(m)]

	for i in range(m):
		for j in range(m):
			conv[i][j]=sum((vectors[i][k]-means[i])*(vectors[j][k]-means[j])for k in range(n))
			conv[i][j]=conv[i][j]/(n-1)

	return conv