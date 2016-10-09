from core import *

#Number of points
nump=10000

#Dataset and its embedding
initial_dataset = create_dataset(200,nump)
jlt_basic_transformed= jlt_basic(initial_dataset,150)
jlt_transformed= jlt_toeplitz(initial_dataset,150)


#Output
plot_distance_performance(initial_dataset,jlt_transformed,0.02)