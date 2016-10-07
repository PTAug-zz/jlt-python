import numpy as np

def create_vector(dim:int):
	"""
	This function returns a gaussian (0,1) vector of dimension dim.
	"""
	return np.random.normal(0,1,dim)

def create_dataset(dim:int,numpoints:int):
	"""
	This function creates numpoints vector created with create_vector.
	"""
	listlol=[]
	[listlol.append(create_vector(dim)) for i in range(numpoints)]
	return listlol