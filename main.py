import moviecredits.connections as connections
import network.heatmap as hm
import network.geometricgraph as gg
import numpy as np
import sys
import csv
from tempfile import TemporaryFile




def main():
    """
    Usage for connections.matrix()

    1.
    the index position represents the index in the array.
    colleagues[0], actors[0] is:
    print(connections_matrix[(0,0)])

    2.
    find index positions where value > 0 and access their values
    colleagues_index, actor_index = np.where(connections_matrix > 0)

    for index in range(len(actor_index)):
        print("colleague {} | actor {}".format(colleagues[colleagues_index[index]], actors[actor_index[index]]))
        print("weight %d "% connections_matrix[(colleagues_index[index], actor_index[index])])
    """
    # actors, colleagues, connections_matrix = connections.matrix()

    adj_matrix, edges = connections.adj_matrix()

    # with open("adj.npy", "wb") as outfile:
    #     np.save(outfile, adj_matrix)
    
    # hm.plot_heatmap(adj_matrix)
    #gg.make_geometric_graph(adj_matrix)

    # with open('actors_colleagues.csv','w+') as csvfile:
    #     comma_out = csv.writer(csvfile, dialect=csv.excel)
    #     for row in adj_matrix:
    #         comma_out.writerow(row)

if __name__ == '__main__':
    main()