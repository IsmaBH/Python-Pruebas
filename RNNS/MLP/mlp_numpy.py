import numpy as np
import random
from random import seed

def init_network(v1):
    w_network = list()
    layers = len(v1)
    for i in range(layers-1):
        w_layer = np.random.randint(1,3,(v1[i+1],v1[i]))
        w_network.append(w_layer)
    return w_network

#Test seccion
v1 = [int (x) for x in input().split()]
weights = init_network(v1)
print(weights)
