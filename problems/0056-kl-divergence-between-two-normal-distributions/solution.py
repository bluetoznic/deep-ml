import numpy as np

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
	KL=np.log(sigma_q/sigma_p)-1/2+(sigma_p**2+(mu_q-mu_p)**2)/(2*(sigma_q**2))
	return float(KL)
