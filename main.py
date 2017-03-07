from moviecredits.datacleaning import INPUT as FILE_DIR
from moviecredits.utils import generate_subset
from moviecredits.utils import generate_all
import moviecredits.connections as connections
# import network.heatmap as hm
import moviecredits.network.makegraph as gg
import pickle
from typing import Set


make = generate_subset.Generate(FILE_DIR, stop=100000)
# make = generate_all.Generate(FILE_DIR)
actor2movies, movie2actors, id2actors, id2movies, movies2id, actors2id = make.connection()
top_actors = make.top_actors(actor2movies)


class Lookup:

    def __init__(self, id2actors, id2movies, movies2id, actors2id, actor2movies, movie2actors):
        """
        :param id2actors: Dict
        :param id2movies: Dict
        :param movies2id: Dict
        :param actors2id: Dict
        :param actor2movies: Defaultdict
        :param movie2actors: Defaultdict
        """
        self.id2actors = id2actors
        self.id2movies = id2movies
        self.movies2id = movies2id
        self.actors2id = actors2id
        self.actor2movies = actor2movies
        self.movie2actors = movie2actors

    def convert_to_actor_name(self, ids: Set):
        return [self.id2actors.get(id) for id in list(ids)]

    def convert_to_movie_name(self, id):
        """id: Integer"""
        return self.id2movies.get(id)

    def movie_cast(self, title):
        """
        Get the cast of relevant movie titles from the given title
        :return the cast of the movies
        """
        casts_id = []

        # find similar titles
        movie_titles = (movie_title for movie_title in self.movies2id.keys() if title in movie_title)

        # get the id
        for movie in movie_titles:
            movie_id = movies2id.get(movie)
            cast_ids = movie2actors.get(movie_id)
            casts_id.append((movie, cast_ids))

            print()
            print(movie)
            for cast_id in cast_ids:
                cast = id2actors.get(cast_id)
                print(cast)

        return casts_id


    def actor(self, name):
        """find the actor id"""

        actor_id = []

        actors = [actor_name for actor_name in self.actors2id.keys() if name in actor_name]
        if actors:
            for actor in actors:
                print("actor", actor, "id:", self.actors2id.get(actor))
                actor_id.append(self.actors2id.get(actor))
            return actor_id
        else:
            exit("Error: no actors named {}".format(name))



    def as_pairs(self):
        # go through the movies
        for _, movies in top_actors.items():
            for movie in movies:

                # convert to names
                print("movieid: {} movie: {}, actorsid: {}, actors: {}".format(movie,
                                                                               self.convert_to_movie_name(movie),
                                                                               self.movie2actors.get(movie),
                                                                               self.convert_to_actor_name(
                                                                                   self.movie2actors.get(movie))))
                # return actors
                pairs = list(make.pair_actors(movie2actors.get(movie)))
                if pairs:
                    print(pairs)
                else:
                    print("skip, only one actor")

    def example(self):

        # go through the movies
        for _, movies in self.actor2movies.items():
            for movie in movies:

                # convert to names
                print("movieid: {} movie: {}, actorsid: {}, actors: {}".format(movie,
                                                                               self.convert_to_movie_name(movie),
                                                                               self.movie2actors.get(movie),
                                                                               self.convert_to_actor_name(
                                                                                   self.movie2actors.get(movie))))

                # return actors
                pairs = list(make.pair_actors(movie2actors.get(movie)))
                if pairs:
                    print(pairs)
                else:
                    print("skip, only one actor")


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

    lookup = Lookup(id2actors, id2movies, movies2id, actors2id, actor2movies, movie2actors)
    casts = lookup.movie_cast('bound')
    actors = lookup.actor('ahmad')

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


    # for index, info in edges.items():
    #         print(index, info.pair, info.weight)

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
    # with open('actors_colleagues.csv','w+') as csvfile:
    #     comma_out = csv.writer(csvfile, dialect=csv.excel)
    #     for row in adj_matrix:
    #         comma_out.writerow(row)

if __name__ == '__main__':
    main()