from moviecredits.datacleaning import INPUT as FILE_DIR
from moviecredits.utils import generate
from typing import Set, Dict
from collections import namedtuple, Counter, defaultdict
import itertools
import pprint

def convert_to_actor_name(ids: Set):
    return [id2actors.get(id) for id in list(ids)]

def convert_to_movie_name(id):
    """ids: Integer"""
    return id2movies.get(id)

# TODO End goal to be able to see the connections like this. In order to create a adjacency matrix
connection = namedtuple('Connection', ['actorA', 'actorB', 'weight'])

class Map_Actors:

    def __init__(self, actor2movies: Dict, movie2actors: Dict):
        self.actor2movies = actor2movies
        self.movie2actors = movie2actors
        self._actor2actors = defaultdict(list)

        self.actor2actors()

    def actor2actors(self):

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


make = generate.Generate(FILE_DIR, stop=100000)

# actors:{movies}
top_actors = make.top_actors()
movie2actors, id2actors, id2movies = make._connection("movie2actors with id2actors")

actor2actors = Map_Actors(top_actors, movie2actors)

print("number of top actors:", len(actor2actors))
print("what the array looks like: ", actor2actors)

for actor, colleagues in actor2actors.item():
    print("actor {} and no. of colleagues {}".format( actor,len(colleagues)))
    for colleague, time_worked_together in colleagues.items():

        # actor pairs with their corresponding weight.
        print(actor, colleague, time_worked_together)




