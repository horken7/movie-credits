import pickle
import moviecredits.connections as connections
import moviecredits.lookup as lookup
import moviecredits.network.makegraph as gg
import numpy as np
from datacleaning import root
import os
import scipy.io as sio
import numpy as np
import csv

# read in all the pickle files.




def main():

    actor2movies, movie2actors, id2actors, id2movies, actors2id, movies2id, top_actors = load_pickle()

    find = lookup.Lookup(id2actors, id2movies, movies2id, actors2id, actor2movies, movie2actors)

    # Finds tuples for all movies matching the search criterias
    casts = find.movie_cast(id2movies.get(12961))
    # Returns a list of all actors ids matching the searched name
    actors = find.actor(id2actors.get(5558))



    # Pick the first movie in the list and convert to array
    colleagues = []
    for i in casts[0][1]:
        colleagues.append(i)

    # Get the first actor in the array
    actor = actors[0]

    # do you want to update the adjacency matrix and edge data, updates if True
    update = True

    if(update):
        adj_matrix, edges = connections.adj_matrix(top_actors, movie2actors)

        # put zeros on the diagonal to make adjacency matrix
        for i in range(0,len(adj_matrix)):
            adj_matrix[i][i] = 0
        print(adj_matrix)

        # save to pickle format
        pickle.dump(adj_matrix, open( "adjacency_matrix.pkl", "wb"))
    else:
        # open pickle file
        adj_matrix = pickle.load(open("adjacency_matrix.pkl", "rb"))
        edges=[1]


    # load_page_ranked_actors(edges)

    # view_heatmap(adj_matrix)

    # make_network(edges, colleague, actor)

    # save_adj_as_csv(adj_matrix)

def load_pickle():
    # First run datacleaning to generate pickle files
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

    return actor2movies, movie2actors, id2actors, id2movies, actors2id, movies2id, top_actors


def load_page_ranked_actors(edges):
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

def save_adj_as_csv(adj_matrix):
    """save adjacency matrix in csv format for page ranking in matlab"""
    with open('actors_colleagues.csv','w+') as csvfile:
        comma_out = csv.writer(csvfile, dialect=csv.excel)
        for row in adj_matrix:
            comma_out.writerow(row)

def view_heatmap(adj_matrix):
    """ run heatmap function"""
    hm.plot_heatmap(adj_matrix)


def make_network(edges, colleagues, actor):

    # run the make graph function
    # with temp data:
    threshold=1
    debug = False # if true will plot each path
    flag = gg.make_graph(edges,colleagues,actor,threshold,debug,update)
    print(flag)
    # if(flag == True):
    #     print('Input is flagged, please check')
    # else:
    #     print('Input passed test, no flags raised')

if __name__ == '__main__':
    main()