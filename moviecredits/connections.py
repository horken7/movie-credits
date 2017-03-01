from moviecredits.datacleaning import INPUT as FILE_DIR
from moviecredits.utils import generate_subset
from moviecredits.utils import generate_all
from typing import Set, Dict
from collections import Counter, defaultdict, namedtuple
import itertools
import array
import numpy as np

actor_pair = namedtuple('Actor_Pair', ['pair', 'weight'])
make = generate_subset.Generate(FILE_DIR, stop=100000)
#make = generate_all.Generate(FILE_DIR)
actor2movies, movie2actors, id2actors, id2movies = make.connection()
top_actors = make.top_actors(actor2movies)

def matrix():
    connections = Matrix(top_actors, movie2actors)
    # the location of the values are changing because the list creation are extracted from unordered data structures.
    # the relative values themselves should not change

    #print(connections.get_actor2actors)
    #print(connections.get_movie2actors)

    return connections.actors, connections.possible_colleagues, connections.get_matrix

def adj_matrix():
    connections = Matrix(top_actors, movie2actors)
    return connections.get_adj_matrix, connections.get_adj_edges

def convert_to_actor_name(ids: Set):
    return [id2actors.get(id) for id in list(ids)]

def convert_to_movie_name(id):
    """ids: Integer"""
    return id2movies.get(id)

# TODO End goal to be able to see the connections like this. In order to create a adjacency matrix

class Map_Actors:

    def __init__(self, actor2movies: Dict, movie2actors: Dict):
        self.actor2movies = actor2movies
        self.movie2actors = movie2actors
        self._actor2actors = defaultdict(list)
        self.actor2actors()

    def actor2actors(self):
        """
        create a {actor: {colleagues:times worked together}}
        """

        # go through the movies
        for actor, movies in self.actor2movies.items():
            for movie in movies:
                # return cast
                cast = list(self.movie2actors.get(movie))
                self._actor2actors[actor].append(cast)

            # join list of lists
            merged_list = list(itertools.chain.from_iterable(self._actor2actors[actor]))

            # count the actors
            times_worked_together = Counter(merged_list)

            self._actor2actors[actor] = times_worked_together

    def item(self):
        return self._actor2actors.items()

    def __len__(self):
        return len(self._actor2actors)

    def __repr__(self):
        return "<Map_actors actor2actors:%s >" % (self._actor2actors)

    def as_pairs(self):
        # go through the movies
        for _, movies in top_actors.items():
            for movie in movies:

                # convert to names
                print("movieid: {} movie: {}, actorsid: {}, actors: {}".format(movie,
                                                                               convert_to_movie_name(movie),
                                                                               movie2actors.get(movie),
                                                                               convert_to_actor_name(
                                                                                   movie2actors.get(movie))))
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
                                                                               convert_to_movie_name(movie),
                                                                               self.movie2actors.get(movie),
                                                                               convert_to_actor_name(
                                                                                   self.movie2actors.get(movie))))

                # return actors
                pairs = list(make.pair_actors(movie2actors.get(movie)))
                if pairs:
                    print(pairs)
                else:
                    print("skip, only one actor")


class Matrix(Map_Actors):

    def __init__(self, top_actors, movie2actors):
        super(Matrix, self).__init__(top_actors, movie2actors)
        self.actors = set()
        self.possible_colleagues = set()

        # build a top actor to colleagues matrix
        self._matrix = self._build_matrix()

        # build adjacency matrix
        self._adj_edges = defaultdict(list)
        self._adj_matrix = self._build_adjacency_matrix()


    @property
    def get_matrix(self):
        return self._matrix

    @property
    def get_adj_matrix(self):
        return self._adj_matrix

    @property
    def get_adj_edges(self):
        return self._adj_edges

    @property
    def get_movie2actors(self):
        return self.movie2actors

    @property
    def get_actor2actors(self):
        return self.actor2movies

    def _build_list(self):
        """
        Build an array for the top_actors (selected actors)
        and build an array for all the possible colleagues are linked to the selected actors
        Use a set to remove duplicates then convert into an array
        """

        for actor, colleagues in super(Matrix, self).item():
            self.actors.add(actor)

            for colleague, _ in colleagues.items():
                self.possible_colleagues.add(colleague)

        self.actors = array.array('i', (self.actors))
        self.possible_colleagues = array.array('i', (self.possible_colleagues))

    def _build_matrix(self):
        """
        Build a matrix of (colleagues against actors) with the weights as the elements
        possible colleagues - row
        top actors - col
        weight - count of the number times the top actor and possible colleagues have worked together in a movie

        it[0] - a feature that allows us to write values to the numpy array while iterating through the array.
        """

        # build possible_colleagues and actors set for rows and cols
        self._build_list()

        # initialise actor against colleagues matrix
        row = len(self.possible_colleagues)
        col = len(self.actors)
        tmp_matrix = np.zeros((row, col), dtype=np.uint32)

        # iterate through matrix
        it = np.nditer(tmp_matrix, flags=['multi_index'], op_flags=['readwrite'])
        while not it.finished:

            # index position
            colleague_index, actor_index = it.multi_index
            actor = self.actors[actor_index]
            possible_colleague = self.possible_colleagues[colleague_index]

            #check if the possible colleague has worked with the top actor
            a = self._actor2actors.get(actor)
            weight = a.get(possible_colleague)

            # Assign the weight
            if weight is not None:
                it[0] = weight
            else:
                # set the weight to 0 when the possible colleague is not associated to actor
                it[0] = 0

            it.iternext()

        return tmp_matrix


    def _build_adjacency_matrix(self):
        """
        Generate a top actors against top actors matrix.
        Note: multi index corresponds to the cartesian product pairs
        and iterating through the matrix matches the cartesian product sequence.
        :return:adj_matrix
        """

        tmp_edges = []

        for edge in self._cartesian_pairs():
            tmp_edges.append(edge)

        # initialise the matrix
        size = len(list(self.actor2movies.keys()))
        tmp_matrix = np.zeros((size, size), dtype=np.uint32)

        # iterate through matrix
        it = np.nditer(tmp_matrix, flags=['multi_index'], op_flags=['readwrite'], order='K')
        while not it.finished:
            # Assign the weight
            it[0] = tmp_edges[it.iterindex].weight

            # save the index with the actor_pairs
            self._adj_edges[it.multi_index] = tmp_edges[it.iterindex]
            it.iternext()
        return tmp_matrix

    def _cartesian_pairs(self):
        "Calculate the cartesian pairs and work out the number of movies they worked together (weight)"

        # generate the cartesian product for the top actors
        actors = list(self.actor2movies.keys())
        product = itertools.product(actors, repeat=2)

        # look up their movies and find the intersection
        for pair in product:
            actorA, actorB = pair
            a = self.actor2movies.get(actorA)
            b = self.actor2movies.get(actorB)
            weight = len(a.intersection(b))
            yield actor_pair(pair, weight)

    def example(self):
        for actor, colleagues in super(Matrix, self).item():
            print("actor {} and no. of colleagues {}".format(actor, len(colleagues)))
            for colleague, time_worked_together in colleagues.items():

                 # actor pairs with their corresponding weight.
                print(actor, colleague, time_worked_together)