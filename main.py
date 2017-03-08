import pickle
import moviecredits.connections as connections
import moviecredits.lookup as lookup
import moviecredits.network.makegraph as gg
from datacleaning import root
import os
import scipy.io as sio
import numpy as np
import csv

# read in all the pickle files.

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

    with open(os.path.join(root, 'actor2movies.pkl'), 'rb') as pklfile:
        actor2movies = pickle.load(pklfile)

    with open(os.path.join(root, 'movie2actors.pkl'), 'rb') as pklfile:
        movie2actors = pickle.load(pklfile)

    with open(os.path.join(root, 'id2actors.pkl'), 'rb') as pklfile:
        id2actors = pickle.load(pklfile)

    with open(os.path.join(root, 'id2movies.pkl'), 'rb') as pklfile:
        id2movies = pickle.load(pklfile)

    with open(os.path.join(root, 'actors2id.pkl'), 'rb') as pklfile:
        actors2id = pickle.load(pklfile)

    with open(os.path.join(root, 'movies2id.pkl'), 'rb') as pklfile:
        movies2id = pickle.load(pklfile)

    with open(os.path.join(root, 'top_actors.pkl'), 'rb') as pklfile:
        top_actors = pickle.load(pklfile)

    print(type(actors2id))

    find = lookup.Lookup(id2actors, id2movies, movies2id, actors2id, actor2movies, movie2actors)
    casts = find.movie_cast('bound')
    actors = find.actor('ahmed')



    # actors, colleagues, connections_matrix = connections.matrix(top_actors, movie2actors)


    adj_matrix, edges = connections.adj_matrix(top_actors, movie2actors)

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

    top_num = sio.loadmat('topNum.mat')
    top_num = top_num['topNum']
    top_num = top_num.flatten()

    for index, info in edges.items():
        print(index, info.pair, info.weight)

    print()
    print("PageRank - Top Actors ID:")
    for top in top_num:
        for index, info in edges.items():
                if top == index[0]:
                    print(info.pair[0])
                    break
    print()



    # run heatmap function
    # hm.plot_heatmap(adj_matrix)


    # create temp data (this will be removed
    colleagues = []
    count=0
    for index, info in edges.items():
        same_node = bool(info.pair[0] == info.pair[1])
        if (info.weight > 0 and not same_node and not info.pair[1] in colleagues and count<6):  # if there is a path between two nodes
            colleagues.append(info.pair[1])
            count+=1
    actor = colleagues[1]
    del colleagues[1]
    print(colleagues)
    print(actor)

    # run the make graph function
    # with temp data:
    # colleagues = [35290,14927,7546]
    # actor = 37756
    threshold = 2
    debug = True # if true will plot each path
    flag = gg.make_graph(edges,colleagues,actor,threshold,debug)
    if(flag == True):
        print('Input is flagged, please check')
    else:
        print('Input passed test, no flags raised')

    # save to csv
    with open('actors_colleagues.csv','w+') as csvfile:
        comma_out = csv.writer(csvfile, dialect=csv.excel)
        for row in adj_matrix:
            comma_out.writerow(row)

if __name__ == '__main__':
    main()