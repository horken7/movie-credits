import csv
import clean.clean as clean
import clean.filetools as filetool
import pickle
import time
from collections import namedtuple, defaultdict

TOTALMOVIES = 1042622
Actor = namedtuple('Actor', ['name', 'extra'])

def main():
    filename = "2017-02-09_223251_ImdbParserOutput/actors.list.tsv" # please change this path to your own file path to the tsv file
    actors_file = "unique_actors.pkl"
    actors = set()
    movies = set()


    actor_dict = defaultdict(list)

    # pre-ready
    filetool.create(actors_file)
    start_time = time.time()
    print("Processing file... This may take a while.")

    with open(filename, mode='r') as file, open(actors_file, mode='wb') as output: # make sure to change 'wb' <<<<<
        reader = csv.reader(file)

        for index ,row in enumerate(reader):
            clean_row = clean.clean(row)
            if clean_row:

                full_name = find_names(clean_row[1], clean_row[0], actors)
                find_movies(clean_row, movies)

                movie = clean_row[2]
                actor_dict[movie].append(Actor(full_name, extra=clean_row[3:])) # we can switch the movie / actor key here.

            # if index > 1000:  # remove these two lines if you want to run through the whole file
            #     break

        pickle.dump(actor_dict, output)

    assert len(actor_dict) == len(movies)

    print("program finished it took {}".format(time.time()-start_time))

def find_names(first_name, last_name, actors):
    if first_name is None:
        name = last_name
        actors.add(name)
        return name
    else:
        name = (first_name + " " + last_name)
        actors.add(name)
        return name


def find_movies(info, movies):
    movie = info[2]
    movies.add(movie)

if __name__ == "__main__":
    main()



