# jlt-python
Implementation of the Johnson–Lindenstrauss transform in Python.

## About the Johnson-Lindenstrauss transform
The Johnson-Lindenstrauss Transform is an embedding of a dataset from a high-dimensional space to a lower-dimensional space, without too much distortion. Dimensionality reduction techniques such as the JLT are used to make handling high-dimensional datasets less time- and memory-consuming.

More information about the JLT can be found [on Wikipedia](https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma).

## About this implementation
This small Python implementation was written to understand the mechanics of the JLT and the precision tradeoff when applying dimensionality reduction techniques. The speed and the memory management are not optimal. For a higher performance, one should use the [scikit-learn Random Projection module](http://scikit-learn.org/stable/modules/random_projection.html).

## How to use
An example is given in [example.py](jlt-python/example.py). 

Each dimension of each datapoint created in a dataset with the function `create_dataset` is taken independently at random from the normal distribution N(0,1). Then the transformation can be applied in 4 different ways:

+ `jlt_basic`: each coefficient of the transformation matrix is taken in N(0,1). It is the most simple way to do it.

+ `jlt_discrete`: each coefficient of the transformation matrix is taken in the {-1,1} set.

+ `jlt_circulant`: the first row of the	transformation matrix is taken at random in N(0,1), and each row is obtained from the previous one by a one-left shift.

+ `jlt_toeplitz`: the first row and column of the transformation matrix is taken at random in N(0,1), and each diagonal has a constant value taken from these first vectors.

Then we evaluate the performance of the reduction by evaluating the ratio of the pairwise vector distance before and after reduction for random pairs of vectors. The `plot_distance_performance` outputs the graphical distribution of this ratio. The smallest the epsilon is, the less distortion there is in the reduction, the better it is.

![alt text](https://github.com/PTAug/jlt-python/tree/master/doc/img/example.png "Output example")