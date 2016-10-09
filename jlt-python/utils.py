import numpy as np
import matplotlib.pyplot as plt


def create_vector(dim: int):
    """
	This function returns a gaussian (0,1) vector of dimension dim.
	"""
    return np.random.normal(0, 1, dim)


def create_dataset(dim: int, numpoints: int):
    """
	This function creates numpoints vector created with create_vector.
	"""
    listvec = []
    [listvec.append(create_vector(dim)) for i in range(numpoints)]
    return listvec


def get_distance(vec1, vec2):
    """
	This function takes two vectors and returns the euclidian
	distance between them.
	"""
    return np.linalg.norm(vec1 - vec2, 2)


def get_random_pairs(dim: int, max_value: int):
    """
	This function returns a list of dim tuples, with random integer values
	between 0 and index_max. The values can't repeat, so dim can't be higher 
	than max_value/2
	"""
    if dim > max_value / 2:
        return []

    index = np.arange(max_value)
    np.random.shuffle(index)
    L = index[:(dim * 2)]
    return [(L[i], L[i + 1]) for i in range(0, len(L), 2)]


def distance_dataset(pairs, dataset):
    """
	This function gives the distances between each pair of vector of dataset
	whose indices are in pairs.
	"""
    list_distance = []
    [list_distance.append(get_distance(dataset[p[0]], dataset[p[1]]))
     for p in pairs]
    return list_distance


def plot_ratio(ratio, precision=0.05):
    """
	This function plots the distribution of the ratio of the distance between two vectors
	before and after the JLT.
	"""
    hist, bin_edges = np.histogram(ratio, bins=np.arange(0, 2, precision))
    plt.bar(bin_edges[:-1], hist, width=precision)
    plt.axvline(x=min(ratio))
    plt.axvline(x=max(ratio))
    plt.xlim(min(bin_edges), max(bin_edges))
    plt.show()
