from utils import *
import math


def jlt_basic(dataset_in,objective_dim):
	jlt=(1/math.sqrt(objective_dim))*np.random.normal(0,1,size=(objective_dim,
		len(dataset_in[0])))
	trans_dataset=[]
	[trans_dataset.append(np.dot(jlt,np.transpose(dataset_in[i]))) 
		for i in range(len(dataset_in))]
	return trans_dataset

def jlt_discrete(dataset_in,objective_dim):
	jlt=(1/math.sqrt(objective_dim))*np.random.choice([-1,1],size=(objective_dim,
		len(dataset_in[0])))
	trans_dataset=[]
	[trans_dataset.append(np.dot(jlt,np.transpose(dataset_in[i]))) 
		for i in range(len(dataset_in))]
	return trans_dataset