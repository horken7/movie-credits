import csv
import pickle
from collections import defaultdict
from ..utils import clean, filehandler
# import pprint


ACTORS_DICT = "actor_dict_lite.pkl"
MOVIE_DICT =  "movie_dict_lite.pkl"

def actor_movie(input):
    """
    Make a dictionary of movie: {actors..}
    Save it into a .pkl file
    :param input: csv
    """

    FILE = 'movie2actor.pkl'
    movie2actors = defaultdict(set)

    # pre-ready
    filehandler.create(FILE)

    print("Processing file... This may take a while.")

    with open(input, mode='r') as file:
        reader = csv.reader(file)

        for index, row in enumerate(reader):
            clean_row = clean.clean(row)

            if clean_row:
                movie = clean_row[2]
                actor_name = full_name(clean_row[1], clean_row[0])

                movie2actors[movie].add(actor_name)

            if index > 100000:  # remove these two lines if you want to run through the whole file
                break

    with open(FILE, mode='wb') as output:
        pickle.dump(movie2actors, output)
    print("Done: Generated movie2actors")


def unique_actor_movie(input):
    """
    Search through the input and generate two files: the name of unique actors and unique movies
    """

    ACTORS_FILE = "unique_actors_lite.pkl"
    MOVIE_FILE = "unique_movie_lite.pkl"

    actors = set()
    movies = set()

    # pre-ready
    filehandler.create(ACTORS_FILE)
    filehandler.create(MOVIE_FILE)

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

    #_generate_id(actors, movies)

    with open(ACTORS_FILE, mode='wb') as output_actors, open(MOVIE_FILE, mode='wb') as output_movie:
        pickle.dump(actors, output_actors)
        pickle.dump(movies, output_movie)

    print("Done: Generated unique actors and unique movies")


def filtered_csv(input):
    """
    produce a csv version of the tsv file and filtering out tv shows and character names
    """

    CSV_FILE = "{}.csv".format(input)

    # pre-ready
    filehandler.create(CSV_FILE)

    print("Processing file... This may take a while.")

    with open(input, mode='r') as file, open(CSV_FILE, mode='w') as output:
        reader = csv.reader(file)

        fieldnames = ['first_name', 'last_name', 'movie']
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        for index, row in enumerate(reader):
            clean_row = clean.clean(row)

            if clean_row:
                #writer.writerow(clean_row)
                writer.writerow({'first_name': clean_row[1], 'last_name': clean_row[0],
                'movie': clean_row[2]})

            if index > 100000:  # remove these two lines if you want to run through the whole file
                break


def _generate_id(actors, movies):
    """
    Generate an id for the movies and actors
    :param actors: set
    :param movies: set
    """
    actor_id = {id: element for id, element in enumerate(actors)}
    movie_id = {id: element for id, element in enumerate(movies)}

    with open(ACTORS_DICT, mode='wb') as actor_d, open(MOVIE_DICT, mode='wb') as movie_d:
        pickle.dump(actor_id, actor_d)
        pickle.dump(movie_id, movie_d)


def full_name(first_name, last_name):
    if first_name is None:
        name = last_name
        return name
    else:
        name = (first_name + " " + last_name)
        return name




