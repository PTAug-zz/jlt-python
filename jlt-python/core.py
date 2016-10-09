from utils import *
import math


def jlt_basic(dataset_in,objective_dim):
	"""
	This function takes the dataset_in and returns the reduced dataset. The 
	output dimension is objective_dim.
	The reduction is done using a basic JLT: each component of the 
	transformation matrix is taken at random in N(0,1).
	"""
	jlt=(1/math.sqrt(objective_dim))*np.random.normal(0,1,size=(objective_dim,
		len(dataset_in[0])))
	trans_dataset=[]
	[trans_dataset.append(np.dot(jlt,np.transpose(dataset_in[i]))) 
		for i in range(len(dataset_in))]
	return trans_dataset

def jlt_discrete(dataset_in,objective_dim):
	"""
	This function takes the dataset_in and returns the reduced dataset. The 
	output dimension is objective_dim.
	The reduction is done using a discrete JLT: each component of the 
	transformation matrix is taken at random in {-1,1}.
	"""
	jlt=(1/math.sqrt(objective_dim))*np.random.choice([-1,1],
		size=(objective_dim,len(dataset_in[0])))
	trans_dataset=[]
	[trans_dataset.append(np.dot(jlt,np.transpose(dataset_in[i]))) 
		for i in range(len(dataset_in))]
	return trans_dataset

def jlt_circulant(dataset_in,objective_dim):
	"""
	This function takes the dataset_in and returns the reduced dataset. The 
	output dimension is objective_dim.
	The reduction is done using a circulant JLT: the first row of the 
	transformation matrix is taken at random in N(0,1), and each row is obtained
	from the previous one by a one-left shift.
	"""
	from scipy.linalg import circulant

	first_row=np.random.normal(0,1,size=(1,len(dataset_in[0])))
	jlt=((1/math.sqrt(objective_dim))*circulant(first_row))[:objective_dim]

	trans_dataset=[]
	[trans_dataset.append(np.dot(jlt,np.transpose(dataset_in[i]))) 
		for i in range(len(dataset_in))]
	return trans_dataset

def jlt_toeplitz(dataset_in,objective_dim):
	"""
	This function takes the dataset_in and returns the reduced dataset. The 
	output dimension is objective_dim.
	The reduction is done using a Toeplitz JLT: the first row and column of the 
	transformation matrix is taken at random in N(0,1), and each diagonal has
	a constant value taken from these first vector
	"""
	from scipy.linalg import toeplitz

	first_row=np.random.normal(0,1,size=(1,len(dataset_in[0])))
	first_column=np.random.normal(0,1,size=(1,objective_dim))
	jlt=((1/math.sqrt(objective_dim))*toeplitz(first_column,first_row))

	trans_dataset=[]
	[trans_dataset.append(np.dot(jlt,np.transpose(dataset_in[i]))) 
		for i in range(len(dataset_in))]
	return trans_dataset
