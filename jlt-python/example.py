from core import *

#Number of points
nump=10000

#Dataset and its embedding
initial_dataset = create_dataset(2000,nump)
jlt_dataset= jlt_basic(initial_dataset,100)

#Performance
index=get_random_pairs(int(nump/2),nump)
tr_dist = distance_dataset(index,jlt_dataset)
init_dist = distance_dataset(index,initial_dataset)

ratio =[]
[ratio.append(tr_dist[i]/init_dist[i]) for i in range(len(index))]

#Output
print(sum(ratio)/len(ratio))
plot_ratio(ratio)