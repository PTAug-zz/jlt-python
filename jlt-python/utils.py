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


def plot_distance_performance(initial_dataset,transformed_dataset, 
        precision=0.05):
    """
	This function plots the distribution of the ratio of the distance between two vectors
	before and after the JLT.
	"""
    index=get_random_pairs(int(len(initial_dataset)/2),len(initial_dataset))
    init_dist = distance_dataset(index,initial_dataset)
    tr_dist = distance_dataset(index,transformed_dataset)
    ratio =[]
    [ratio.append(tr_dist[i]/init_dist[i]) for i in range(int(len(index)))]
    max_ratio = max(ratio)
    min_ratio = min(ratio)
    epsilon=(max([abs(1-min_ratio),(1-max_ratio)]))
    print(epsilon)

    hist, bin_edges = np.histogram(ratio, bins=np.arange(0, 2, precision))
    fig=plt.figure()
    fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    ax.set_title('axes title')

    ax.text(0.98, 0.98,'$\epsilon=$%.3f'%epsilon, fontsize=15,
        verticalalignment='top', horizontalalignment='right',
        transform=ax.transAxes)
    ax.bar(bin_edges[:-1], hist, width=precision,color='#eeefff')
    ax.axvline(x=min_ratio,c='r',label=('Min=%.3f'%(min_ratio)))
    ax.axvline(x=max_ratio,c='g',label=('Max=%.3f'%(max_ratio)))

    ax.legend(loc='upper left')
    plt.xlim(min(bin_edges), max(bin_edges))
    plt.show()
