import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import time
def make_graph(edges,colleagues,actor,threshold,debug): #removed 'edges' while pickled graph
	G = nx.Graph()

	for index, info in edges.items():
		if(info.weight>0 and info.pair[0] != info.pair[1]): # if there is a path between two nodes
			G.add_edge(info.pair[0], info.pair[1], weight=1000-info.weight) # invert weight to get longest path

	nx.write_gpickle(G,open( "graph.pkl", "wb"))

	# read pickled graph
	# G = nx.read_gpickle(open("graph.pkl", "rb"))


	# calculate the shortest (longest) path between the actor and each colleague and save in longest_path
	longest_path = []
	for colleague in colleagues:
		if(nx.has_path(G,colleague,actor)):
			shortest = nx.dijkstra_path_length(G, colleague, actor)
			path = nx.dijkstra_path(G, colleague, actor)
			if(debug == True):
				plot_graph(G,path)
			tmp = len(path) - 1 # first element is start node
			howlong = abs(shortest - tmp * 1000) # the length of the longest path
			longest_path.append(howlong)
		else:
			longest_path.append(0)

	# if the mean path is shorter then some threshold then flag
	if np.mean(longest_path) > threshold:
		return False
	else:
		return True

def plot_graph(G,p):
	# reset colors
	for e in G.edges():
		G[e[0]][e[1]]['color'] = 'black'

	# set path colors
	for i in range(len(p) - 1):
		G[p[i]][p[i + 1]]['color'] = 'red'

	# Store in a list to use for drawing
	edge_color_list = [G[e[0]][e[1]]['color'] for e in G.edges()]

	pos = nx.spring_layout(G) # positioning layout

	path = []
	for i in range(len(p)-1):
		path.append((p[i],p[i+1])) # path list for printing

	# nx.draw(G, pos, node_size=1, edge_size=1, edge_color=edge_color_list)
	nx.draw(G, pos, node_size=1, edge_size=1, edge_color=edge_color_list)
	nx.draw_networkx_edges(G, pos, edgelist=path, node_size=1, edge_size=1, edge_color='r', width=1.0) # print the path on top
	plt.show()
