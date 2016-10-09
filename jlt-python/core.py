from utils import *
import math


def jlt_basic(dataset_in,objective_dim):
	jlt=(1/math.sqrt(objective_dim))*np.random.rand(len(dataset_in[0]),
		objective_dim)
	trans_dataset=[]
	[trans_dataset.append(np.dot(dataset_in[i],jlt)) 
		for i in range(len(dataset_in))]
	return trans_dataset