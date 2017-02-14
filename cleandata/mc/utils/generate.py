import csv
import pickle
import time
from ..utils import clean, filehandler

ACTORS_FILE = "unique_actors_lite.pkl"
MOVIE_FILE = "unique_movie_lite.pkl"

ACTORS_DICT = "actor_dict_lite.pkl"
MOVIE_DICT =  "movie_dict_lite.pkl"




def actor_movie(input):
    """
    Search through the input and generate two files: the name of unique actors and unique movies
    """

    actors = set()
    movies = set()

    # pre-ready
    filehandler.create(ACTORS_FILE)
    filehandler.create(MOVIE_FILE)

    start_time = time.time()
    print("Processing file... This may take a while.")

    with open(input, mode='r') as file:
        reader = csv.reader(file)

        for index, row in enumerate(reader):
            clean_row = clean.clean(row)

            if clean_row:
                movie = clean_row[2]
                actor_name = full_name(clean_row[1], clean_row[0])

                actors.add(actor_name)
                movies.add(movie)

            if index > 100000:  # remove these two lines if you want to run through the whole file
                break

    with open(ACTORS_FILE, mode='wb') as output_actors, open(MOVIE_FILE, mode='wb') as output_movie:
        pickle.dump(actors, output_actors)
        pickle.dump(movies, output_movie)

    _generate_id(actors, movies)


    print("program generate.py finished, it took {}".format(time.time() - start_time))


def _generate_id(actors, movies):
    actor_dict = {id: element for id, element in enumerate(actors)}
    id_dict = {id: element for id, element in enumerate(movies)}

    with open(ACTORS_DICT, mode='wb') as actor_d, open(MOVIE_DICT, mode='wb') as movie_d:
        pickle.dump(actor_dict, actor_d)
        pickle.dump(id_dict, movie_d)


def full_name(first_name, last_name):
    if first_name is None:
        name = last_name
        return name
    else:
        name = (first_name + " " + last_name)
        return name


