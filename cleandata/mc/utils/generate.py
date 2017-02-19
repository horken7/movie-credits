import csv
import pickle
from collections import defaultdict
from ..utils import clean, filehandler
# import pprint


class Generate:

    def __init__(self, file, stop=1000):
        self.input = file
        self.stop = stop

    def actor_movie(self):
        """
        Make a dictionary of movie: {actors..}
        and actor: {movies}
        Save it into a .pkl file
        """

        # TODO currently we are saving a lot of files into memory and reading it again, if we change this part of code.
        # we can output the lines one by one e.g. a clean line, in the desired format because don't really need to
        # manipulate these.

        FILE1 = 'movie2actor.pkl'
        FILE2 = 'actor2movie.pkl'
        movie2actors = defaultdict(set)
        actor2movies = defaultdict(set)

        # make sure file exist
        filehandler.create(FILE1)
        filehandler.create(FILE2)

        print("Processing file... This may take a while.")

        with open(self.input, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)

            for index, row in enumerate(reader):
                clean_row = clean.clean(row)

                if clean_row:
                    movie = clean_row[2]
                    actor_name = full_name(clean_row[1], clean_row[0])

                    movie2actors[movie].add(actor_name)
                    actor2movies[actor_name].add(movie)

                if index > self.stop:  # remove these two lines if you want to run through the whole file
                    break

        with open(FILE1, mode='wb') as output1, open(FILE2, mode='wb') as output2:
            pickle.dump(movie2actors, output1)
            pickle.dump(actor2movies, output2)
        print("Done: Generated movie2actors and actor2movies")

    def unique_actor_movie(self):
        """
        Search through the input and generate two files: the name of unique actors and unique movies
        """

        ACTORS_FILE = "unique_actors_lite.pkl"
        MOVIE_FILE = "unique_movie_lite.pkl"

        actors = set()
        movies = set()

        # make sure file exist
        filehandler.create(ACTORS_FILE)
        filehandler.create(MOVIE_FILE)

        print("Processing file... This may take a while.")

        with open(self.input, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)

            for index, row in enumerate(reader):
                clean_row = clean.clean(row)

                if clean_row:
                    movie = clean_row[2]
                    actor_name = full_name(clean_row[1], clean_row[0])

                    actors.add(actor_name)
                    movies.add(movie)

                if index > self.stop:  # remove these two lines if you want to run through the whole file
                    break

        #_generate_id(actors, movies)

        with open(ACTORS_FILE, mode='wb') as output_actors, open(MOVIE_FILE, mode='wb') as output_movie:
            pickle.dump(actors, output_actors)
            pickle.dump(movies, output_movie)

        print("Done: Generated unique actors and unique movies")

    def filtered_csv(self):
        """
        produce a csv version of the tsv file and filtering out tv shows and character names
        """

        CSV_FILE = "{}.csv".format(self.input)

        # make sure file exist
        filehandler.create(CSV_FILE)

        print("Processing file... This may take a while.")

        with open(self.input, mode='r', encoding='utf-8') as file, open(CSV_FILE, mode='w') as output:
            reader = csv.reader(file)

            fieldnames = ['first_name', 'last_name', 'movie']
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()

            for index, row in enumerate(reader):
                clean_row = clean.clean(row)

                if clean_row:
                    writer.writerow({'first_name': clean_row[0], 'last_name': clean_row[1],
                    'movie': clean_row[2]})

                if index > self.stop:  # remove these two lines if you want to run through the whole file
                    break

        print("Done: cleaned up tsv and made a csv")

    def top_actors(self):
        """
        Find the amount of movies completed for each actor and threshold to find the popular actors.
        @:param: JSON like object for actor -> {movies}
        :return: a list of the top actors
        """
        pass

    def _generate_id(self, actors, movies):
        """
        Generate an id for the movies and actors
        :param actors: set
        :param movies: set
        """
        ACTORS_DICT = "actor_dict_lite.pkl"
        MOVIE_DICT = "movie_dict_lite.pkl"

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




