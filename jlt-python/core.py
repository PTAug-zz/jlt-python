from utils import *

nump=100
a = create_dataset(20,nump)

index=get_random_pairs(50,nump)

print(distance_dataset(index,a))
