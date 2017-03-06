import numpy as np
import network.geometricgraph as gg
import scipy.io

"""made for dealing with a large matrix, rather than having to build the large matrix everytime"""

with open("adj.npy", mode='rb') as inputfile:
	adj_matrix = np.load(inputfile)

for i in range(len(adj_matrix)):
	adj_matrix[(i,i)] = 0
	#print(adj_matrix[(i,i)])

scipy.io.savemat('test.mat', dict(x=adj_matrix))
