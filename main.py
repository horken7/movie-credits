import moviecredits.connections as connections
# import network.heatmap as hm
import network.makegraph as gg
# import numpy as np
# import sys
# import csv
# from tempfile import TemporaryFile
import pickle


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

    # put zeros on the diagonal to make adjacency matrix
    for i in range(0,len(adj_matrix)):
        adj_matrix[i][i] = 0
    print(adj_matrix)


    # save to pickle format
    pickle.dump(adj_matrix,open( "adjacency_matrix.pkl", "wb"))

    # open pickle file
    # if you want to use the pickled file without having to run the entire program
    # remember to comment out the import files
    # adj_matrix = pickle.load(open("adjacency_matrix.pkl", "rb"))
    # edges = pickle.load(open("edges.pkl", "rb"))
    # for index, info in edges.items():
    #         print(index, info.pair, info.weight)

    # run heatmap function
    # hm.plot_heatmap(adj_matrix)

    # run the make graph function
    # with temp data:
    colleagues = [402992,115624,379731,41344,135259]
    actor = 88316
    threshold = 2
    debug = True # if true will plot each path
    flag = gg.make_graph(edges,colleagues,actor,threshold,debug) #removed 'edges' while pickled graph

    if(flag == True):
        print('Input is flagged, please check')
    else:
        print('Input passed test, no flags raised')

    # save to csv
    # with open('actors_colleagues.csv','w+') as csvfile:
    #     comma_out = csv.writer(csvfile, dialect=csv.excel)
    #     for row in adj_matrix:
    #         comma_out.writerow(row)

if __name__ == '__main__':
    main()