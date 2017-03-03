#import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def make_graph(adj_matrix,colleagues,actor,mapping,threshold):
	G=nx.from_numpy_matrix(adj_matrix)

	# uncomment to visulise the network
	# nx.draw(G, node_size=1, edge_size=1, with_labels=False)
	# plt.show()

	# map from 'mapping' to the indexes used in the Graph
	actors_index = []
	for a in colleagues:
		for index, item in enumerate(mapping):
			if item == a:
				actors_index.append(index)
			if item == actor:
				my_actor = index

	# calculate the shortest path between the actor and each colleague and save in longest_path
	longest_path = []
	for curr in actors_index:
		if(nx.has_path(G,curr,my_actor)):
			shortest = nx.dijkstra_path_length(G, curr, my_actor)
			path = nx.dijkstra_path(G, curr, my_actor)
			tmp = len(path) - 1
			howlong = abs(shortest - tmp * 1000) # the length of the longest path
			longest_path.append(howlong)
		else:
			longest_path.append(0)

	# if the mean path is shorter then some threshold then flag
	if np.mean(longest_path) > threshold:
		return 0
	else:
		return 1
