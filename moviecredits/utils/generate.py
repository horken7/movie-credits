import csv
import pickle
from collections import defaultdict, namedtuple
from itertools import product, zip_longest
from typing import Set
from moviecredits.utils import clean, filehandler


class Generate:

    def __init__(self, file, stop=1000):
        self.input = file
        self.stop = stop

    def _connection(self, option):
        """
        Make a dictionary of movie: {actors} and actor: {movies}
        :return actor2movies and movie2actors
        """
        file1 = 'unique_actors_lite.pkl'
        file2 = 'unique_movie_lite.pkl'

        # create required pkl files
        self.unique_actor_movie()

        actor2movies = defaultdict(set)
        movie2actors = defaultdict(set)

        with open(file1, 'rb') as actors, open(file2, 'rb') as movies:
            a = pickle.load(actors)
            b = pickle.load(movies)

        actors2id, id2actors = self._generate_id(a)
        movies2id, id2movies = self._generate_id(b)

        clean_csv = self.input + '.csv'

        with open(clean_csv, mode='r', encoding='utf-8') as file:
            next(file) # skip first line
            reader = csv.reader(file)

            for index, row in enumerate(reader):

                movie = row[2]
                actor_name = full_name(row[1], row[0])

                # lookup id
                actor_name = actors2id.get(actor_name)
                movie = movies2id.get(movie)

                # populate with id equivalent
                actor2movies[actor_name].add(movie)
                movie2actors[movie].add(actor_name)

                if index > self.stop:  # remove these two lines if you want to run through the whole file
                    break

        print("Done: generating connections {}", option)

        if option == 'actor2movies':
            return actor2movies
        elif option == "movie2actors":
            return movie2actors
        elif option == "movie2actors with id2actors":
            return movie2actors, id2actors, id2movies

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

        clean_csv = self.input + '.csv'

        # create required clean csv
        self.filtered_csv()

        print("Processing file... This may take a while.")

        with open(clean_csv, mode='r', encoding='utf-8') as file:
            next(file) #skip first line
            reader = csv.reader(file)

            for index, row in enumerate(reader):

                movie = row[2]
                actor_name = full_name(row[1], row[0])

                actors.add(actor_name)
                movies.add(movie)

                if index > self.stop:  # remove these two lines if you want to run through the whole file
                    break

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
        """Find the amount of movies completed for each actor and threshold to find the popular actors."""
        print("finding top actors")
        a = self._connection("actor2movies")

        # find actors who was in more than 100 movies.
        top_actor = {actor: movies for actor, movies in a.items() if len(movies) > 70 and len(movies) < 80}
        return top_actor

    def pair_actors(self, cast: Set):
        """
        pair actors from a given dataset
        :return: pair actors
        """
        if len(cast) <= 1:
            return None

        # use combinations to generate the index values
        pairs = list(product([value for value in range(len(cast))], repeat=2))

        for pair in pairs:
            a,b = pair
            actors = list(cast)
            yield(actors[a], actors[b])

    def _generate_id(self, items):
        """
        input: sequence or set
        return a dictionary {items:id} and the inverse {id:items}
        """
        item2id = {item: id for id, item in enumerate(items)}
        id2item = dict( zip_longest(item2id.values(), item2id.keys()) )
        return item2id, id2item


def full_name(first_name, last_name):
    if first_name is None:
        name = last_name
        return name
    else:
        name = (first_name + " " + last_name)
        return name
