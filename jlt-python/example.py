from core import *

#Number of points
nump=10000
dim_init=1000
obj_dim=100

#Dataset and its embedding
initial_dataset = create_dataset(dim_init,nump)
jlt_basic_transformed= jl_transform(initial_dataset,obj_dim,"basic")
jlt_discrete_transformed= jl_transform(initial_dataset,obj_dim,"discrete")
jlt_circulant_transformed= jl_transform(initial_dataset,obj_dim,"circulant")
jlt_toeplitz_transformed= jl_transform(initial_dataset,obj_dim,"toeplitz")

#Pairs chosen
index=get_random_pairs(int(len(initial_dataset)/2),len(initial_dataset))

#Distance between paired vectors
init_dist = distance_dataset(index,initial_dataset)
tr_basic_dist = distance_dataset(index,jlt_basic_transformed)
tr_discrete_dist = distance_dataset(index,jlt_discrete_transformed)
tr_circulant_dist = distance_dataset(index,jlt_circulant_transformed)
tr_toeplitz_dist = distance_dataset(index,jlt_toeplitz_transformed)

#Ratios
ratio_basic =[]
[ratio_basic.append(tr_basic_dist[i]/init_dist[i]) for i in range(int(len(index)))]
ratio_discrete =[]
[ratio_discrete.append(tr_discrete_dist[i]/init_dist[i]) for i in range(int(len(index)))]
ratio_circulant =[]
[ratio_circulant.append(tr_circulant_dist[i]/init_dist[i]) for i in range(int(len(index)))]
ratio_toeplitz =[]
[ratio_toeplitz.append(tr_toeplitz_dist[i]/init_dist[i]) for i in range(int(len(index)))]

#Ratio Stats
max_ratio_basic = max(ratio_basic)
min_ratio_basic = min(ratio_basic)
epsilon_basic=(max([abs(1-min_ratio_basic),abs(1-max_ratio_basic)]))

max_ratio_discrete = max(ratio_discrete)
min_ratio_discrete = min(ratio_discrete)
epsilon_discrete=(max([abs(1-min_ratio_discrete),abs(1-max_ratio_discrete)]))

max_ratio_circulant = max(ratio_circulant)
min_ratio_circulant = min(ratio_circulant)
epsilon_circulant=(max([abs(1-min_ratio_circulant),abs(1-max_ratio_circulant)]))

max_ratio_toeplitz = max(ratio_toeplitz)
min_ratio_toeplitz = min(ratio_toeplitz)
epsilon_toeplitz=(max([abs(1-min_ratio_toeplitz),abs(1-max_ratio_toeplitz)]))

#Output
#plot_distance_performance(initial_dataset,jlt_transformed,0.02)
precision=0.02

f, ((ax1, ax2), (ax3,ax4)) = plt.subplots(2,2, sharex='col', sharey='row')
	
f.suptitle('Ratio of the pairwise vector distance before and after reduction, for %s points from dimension %s to dimension %s'%(nump,dim_init,obj_dim),
  	fontsize=14, fontweight='bold')
f.subplots_adjust(top=0.85)

hist1, bin_edges1 = np.histogram(ratio_basic, bins=np.arange(0, 2, precision))
hist2, bin_edges2 = np.histogram(ratio_discrete, bins=np.arange(0, 2, precision))
hist3, bin_edges3 = np.histogram(ratio_circulant, bins=np.arange(0, 2, precision))
hist4, bin_edges4 = np.histogram(ratio_toeplitz, bins=np.arange(0, 2, precision))

ax1.set_title('Basic JLT')
ax1.text(0.98, 0.98,'$\epsilon=$%.3f'%epsilon_basic, fontsize=15,
    verticalalignment='top', horizontalalignment='right',
    transform=ax1.transAxes)
ax1.bar(bin_edges1[:-1], hist1, width=precision,color='#eeefff')
ax1.axvline(x=min_ratio_basic,c='r',label=('Min=%.3f'%(min_ratio_basic)))
ax1.axvline(x=max_ratio_basic,c='g',label=('Max=%.3f'%(max_ratio_basic)))
ax1.legend(loc='upper left')

ax2.set_title('Discrete JLT')
ax2.text(0.98, 0.98,'$\epsilon=$%.3f'%epsilon_discrete, fontsize=15,
    verticalalignment='top', horizontalalignment='right',
    transform=ax2.transAxes)
ax2.bar(bin_edges2[:-1], hist2, width=precision,color='#eeefff')
ax2.axvline(x=min_ratio_discrete,c='r',label=('Min=%.3f'%(min_ratio_discrete)))
ax2.axvline(x=max_ratio_discrete,c='g',label=('Max=%.3f'%(max_ratio_discrete)))
ax2.legend(loc='upper left')

ax3.set_title('Circulant JLT')
ax3.text(0.98, 0.98,'$\epsilon=$%.3f'%epsilon_circulant, fontsize=15,
    verticalalignment='top', horizontalalignment='right',
    transform=ax3.transAxes)
ax3.bar(bin_edges3[:-1], hist3, width=precision,color='#eeefff')
ax3.axvline(x=min_ratio_circulant,c='r',label=('Min=%.3f'%(min_ratio_circulant)))
ax3.axvline(x=max_ratio_circulant,c='g',label=('Max=%.3f'%(max_ratio_circulant)))
ax3.legend(loc='upper left')

ax4.set_title('Toeplitz JLT')
ax4.text(0.98, 0.98,'$\epsilon=$%.3f'%epsilon_toeplitz, fontsize=15,
    verticalalignment='top', horizontalalignment='right',
    transform=ax4.transAxes)
ax4.bar(bin_edges4[:-1], hist4, width=precision,color='#eeefff')
ax4.axvline(x=min_ratio_toeplitz,c='r',label=('Min=%.3f'%(min_ratio_toeplitz)))
ax4.axvline(x=max_ratio_toeplitz,c='g',label=('Max=%.3f'%(max_ratio_toeplitz)))
ax4.legend(loc='upper left')

plt.show()