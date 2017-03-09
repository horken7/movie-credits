import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
def make_graph(edges,colleagues, actor, threshold, debug, update): #removed 'edges' while pickled graph
    # if you want to update the graph
    if(update==True):
        G = nx.Graph()

        for index, info in edges.items():
            same_node = bool(info.pair[0] == info.pair[1])
            if(info.weight>0 and not same_node): # if there is a path between two nodes
            # if (not same_node):
                G.add_edge(info.pair[0], info.pair[1], weight=1000-info.weight) # invert weight to get longest path

        nx.write_gpickle(G,open( "graph.pkl", "wb"))
    else:
        # read pickled graph
        G = nx.read_gpickle(open("graph.pkl", "rb"))

    # calculate the shortest (longest) path between the actor and each colleague and save in longest_path
    longest_path = []
    path_length = []
    # del colleagues[0]
    # for colleague in colleagues:
    #     G.remove_edge(actor,colleague)

    # pos = nx.spring_layout(G)  # positioning layout
    # nx.draw_networkx(G, pos, node_size=1, edge_size=1, with_labels=True, font_size=6)  # print entire graph
    # # nx.draw_networkx_nodes(G, pos, nodelist=colleagues, node_size=25, node_color='g')  # mark actor in blue
    # nx.draw_networkx_nodes(G, pos, nodelist=[7809], node_size=25, node_color='b')  # mark actor in blue
    # plt.show()

    for colleague in colleagues:
        try:
            if nx.has_path(G, colleague, actor):
                shortest = nx.dijkstra_path_length(G, colleague, actor)
                path = nx.dijkstra_path(G, colleague, actor)
                if(debug == True):
                    plot_graph(G,path,actor,colleague)
                tmp = len(path) - 1 # first element is start node
                howlong = abs(shortest - tmp * 1000) # the length of the longest path
                path_length.append(len(path))
                longest_path.append(howlong)

            else:
                longest_path.append(0)
        except nx.NetworkXError as e:
            print(e)
            print("Error, you fucked up")


    return longest_path, path_length
    # if the mean path is shorter then some threshold then flag
    # if np.mean(longest_path) > threshold:
    #     return False
    # else:
    #     return True

def plot_graph(G,p,actor,colleauge):
    pos = nx.spring_layout(G) # positioning layout

    path = []
    for i in range(len(p)-1):
        path.append((p[i],p[i+1])) # path list for printing

    nx.draw_networkx(G, pos, node_size=1, edge_size=1,with_labels=False,font_size=2) # plot entire graph
    nx.draw_networkx_edges(G, pos, edgelist=path,edge_color='r') # mark path in red
    nx.draw_networkx_nodes(G, pos, nodelist=[actor], node_size=25, node_color='b') # mark actor in blue
    nx.draw_networkx_nodes(G, pos, nodelist=[colleauge], node_size=25, node_color='g') # mark colleague in green
    plt.show()
