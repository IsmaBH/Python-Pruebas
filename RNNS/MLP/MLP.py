#This is a simple implementation of the MLP network
import numpy as np

print("MLP net")

#At first we generate our training set
p = np.arange(-2, 2, 0.1)
G = 1 + np.sin((np.pi*p)/4)
print(p)
print(G)