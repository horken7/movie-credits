from moviecredits.datacleaning import INPUT as FILE_DIR
from moviecredits.utils import generate
from typing import Set

def convert_to_actor_name(ids: Set):
    return [id2actors.get(id) for id in list(ids)]

def convert_to_movie_name(id):
    """ids: Integer"""
    return id2movies.get(id)


make = generate.Generate(FILE_DIR, stop=100000)

# actors:{movies}
top_actors = make.top_actors()

movie2actors, id2actors, id2movies = make._connection("movie2actors with id2actors")

# go through the movies
for _, movies in top_actors.items():
    for movie in movies:

        # convert to names
        print("movieid: {} movie: {}, actorsid: {}, actors: {}".format(movie,
                                                                       convert_to_movie_name(movie),
                                                                       movie2actors.get(movie),
                                                                       convert_to_actor_name(movie2actors.get(movie))))
        # return actors
        pairs = list(make.pair_actors(movie2actors.get(movie)))
        if pairs:
            print(pairs)
        else:
            print("skip, only one actor")
