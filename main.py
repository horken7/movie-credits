import moviecredits.connections as connections
import network.heatmap as hm
import network.geometricgraph as gg
import numpy as np

import sys
import csv



def main():
    actors, colleagues, connections_matrix = connections.matrix()
    print(connections_matrix)

    # # next... to output the previous output examples to complement the matrix.

    # # the index position represents the index in the array.
    # # colleagues[0], actors[0] is:
    
    # print(connections_matrix[(0,0)])
    # print()

    # # index positions value > 0
    # colleagues_index, actor_index = np.where(connections_matrix > 0)

    # for index in range(len(actor_index)):
    #    print("colleague {} | actor {}".format(colleagues[colleagues_index[index]], actors[actor_index[index]]))
    #    print("weight %d "% connections_matrix[(colleagues_index[index], actor_index[index])])

    #hm.plot_heatmap(connections_matrix)
    #gg.make_geometric_graph(connections_matrix)

    # sz = np.shape(connections_matrix)
    # mtx=np.zeros((max(sz), max(sz)), dtype=np.uint32)
    # mtx[0:sz[0],0:sz[1]]=connections_matrix
    # gg.make_geometric_graph(mtx)

    # with open('actors_colleagues.csv','w+') as csvfile:
    #     comma_out = csv.writer(csvfile, dialect=csv.excel)
    #     for row in connections_matrix:
    #         comma_out.writerow(row)












if __name__ == '__main__':
    main()